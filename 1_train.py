import torch
import torchvision.models as models
import torch.nn as nn

print("Initializing MobileNetV2 architecture...")

model = models.mobilenet_v2(weights='DEFAULT')

model.classifier[1] = nn.Linear(model.last_channel, 2)

torch.save(model.state_dict(), "safety.pth")
print("✅ Success: 'safety.pth' created in your folder!")