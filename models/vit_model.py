import torch
import timm
import torch.nn as nn

class ViTModel(nn.Module):
    def __init__(self, num_classes=2):
        super(ViTModel, self).__init__()
        self.model = timm.create_model("vit_base_patch16_224", pretrained=True, num_classes=num_classes)

    def forward(self, x):
        return self.model(x)

# Example usage
if __name__ == "__main__":
    model = ViTModel()
    print(model)
