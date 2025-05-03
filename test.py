import torch
from torchvision import transforms
from PIL import Image
import os
from tqdm import tqdm  # Progress bar
from models.vit_model import ViTModel

# Load model
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = ViTModel(num_classes=2).to(device)
model.load_state_dict(torch.load("vit_morphing_detector.pth", map_location=device))
model.eval()

# Define transform
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5]),
])

def predict(image_path):
    image = Image.open(image_path).convert("RGB")
    image = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        output = model(image)
        prediction = torch.argmax(output, dim=1).item()
    
    return prediction  # 1 = Morph, 0 = Not Morph

def evaluate_model(test_folder):
    correct = 0
    total = 0

    # Define test subfolders
    morph_folder = os.path.join(test_folder, "morph")
    not_morph_folder = os.path.join(test_folder, "not_morph")

    # Get total number of images
    all_images = [(os.path.join(morph_folder, img), 1) for img in os.listdir(morph_folder)] + \
                 [(os.path.join(not_morph_folder, img), 0) for img in os.listdir(not_morph_folder)]
    
    # Iterate with progress bar
    for img_path, label in tqdm(all_images, desc="Evaluating", unit="image"):
        if predict(img_path) == label:  
            correct += 1
        total += 1

    # Calculate Accuracy
    accuracy = (correct / total) * 100
    print(f"\nModel Accuracy on Test Set: {accuracy:.2f}%")

# Run evaluation
evaluate_model("dataset/test")
