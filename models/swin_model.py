import torch
import timm
import torch.nn as nn

class SwinModel(nn.Module):
    def __init__(self, num_classes=2):
        super(SwinModel, self).__init__()
        self.model = timm.create_model("swin_base_patch4_window7_224", pretrained=True, num_classes=num_classes)

    def forward(self, x):
        return self.model(x)

# Example usage
if __name__ == "__main__":
    model = SwinModel()
    print(model)
