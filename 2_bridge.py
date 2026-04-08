import torch
import torchvision.models as models
import torch.nn as nn

model = models.mobilenet_v2()
model.classifier[1] = nn.Linear(model.last_channel, 2)

model.load_state_dict(torch.load("safety.pth"))
model.eval()

print("🚀 Exporting to ONNX...")
dummy_input = torch.randn(1, 3, 224, 224)
torch.onnx.export(model, dummy_input, "model.onnx", input_names=['input'], output_names=['output'])
print("✅ SUCCESS: 'model.onnx' updated with new training!")