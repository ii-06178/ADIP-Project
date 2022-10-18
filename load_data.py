from email.mime import image
from torch.utils.data import DataLoader
import torchvision.utils as vutils
from torchvision import datasets, transforms
import matplotlib.pyplot as plt
import numpy as np

#loads from folder
dataset = datasets.ImageFolder(root="G:\ADIP\Project\data\data_set",
                           transform=transforms.ToTensor())
# Create the dataloader
dataloader = DataLoader(dataset, batch_size=1, shuffle=True)

#to iterate
images= next(iter(dataloader))
plt.figure(figsize=(8,8))
plt.title("Images")
plt.imshow(np.transpose(vutils.make_grid(images[0][:50], padding=2, normalize=True),(1,2,0))) #loads 50th image
print((images[1][:50]).item())  #label of 50th image


#This is just a temporary code to show a picture of Williams and Fragile X
w_flag=False
f_flag=False
for batch in dataloader:
    if batch[1].item()==0 and f_flag==False:
        plt.figure(figsize=(8,8))
        plt.title("Fragile X")
        plt.imshow(np.transpose(vutils.make_grid(batch[0], padding=2, normalize=True),(1,2,0)))
        f_flag=True
    if batch[1].item()==2 and w_flag==False:
        plt.figure(figsize=(8,8))
        plt.title("Williams")
        plt.imshow(np.transpose(vutils.make_grid(batch[0], padding=2, normalize=True),(1,2,0)))
        w_flag=True


plt.show()

#prints classes, in our case it's 3
print(dataset.classes)
print(dataset.class_to_idx)
