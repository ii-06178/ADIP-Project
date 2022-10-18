#To bring uniformity in naming convention of images

import os
file_id=0
#for williams
for i in os.listdir("C:\\Users\\D\\Downloads\\williams"):
    
    file_id+=1 
    os.rename(f'C:\\Users\\D\\Downloads\\williams\\{i}',f'C:\\Users\\D\\Downloads\\williams\\{file_id}.jpg')

#for normal
for i in os.listdir("C:\\Users\\D\\Downloads\\crop_part1\\crop_part1"):
    
    file_id+=1 
    os.rename(f'C:\\Users\\D\\Downloads\\crop_part1\\crop_part1\\{i}',f'C:\\Users\\D\\Downloads\\crop_part1\\crop_part1\\{file_id}.jpg')