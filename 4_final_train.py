import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms, models
from torch.utils.data import DataLoader
import os

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.RandomHorizontalFlip(p=0.5), 
    transforms.RandomRotation(15),           
    transforms.ColorJitter(brightness=0.3, contrast=0.3), 
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

if not os.path.exists('dataset'):
    print("❌ Error: 'dataset' folder not found!")
else:
    train_data = datasets.ImageFolder('dataset', transform=transform)
    train_loader = DataLoader(train_data, batch_size=4, shuffle=True)
    print(f"✅ Found {len(train_data)} images. Classes: {train_data.classes}")

model = models.mobilenet_v2(weights='DEFAULT')
model.classifier[1] = nn.Linear(model.last_channel, 2) 

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.0001) 

print("🚀 Training starting... (3-5 minutes)")
model.train()
for epoch in range(20): 
    running_loss = 0.0
    for images, labels in train_loader:
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        running_loss += loss.item()
    
    avg_loss = running_loss/len(train_loader)
    print(f"Epoch {epoch+1}/20 - Loss: {avg_loss:.4f}")

torch.save(model.state_dict(), "safety.pth")
print("\n✅ SUCCESS: 'safety.pth' is now trained!")