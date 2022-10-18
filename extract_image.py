#code to extract images of those who are in btw 7-16 years old


import os
for i in os.listdir("C:\\Users\\D\\Downloads\\crop_part1\\crop_part1"):
    split=i.split('_')
    age=int(split[0])
    if age<6 or age >13:
        
        os.remove(f'C:\\Users\\D\\Downloads\\crop_part1\\crop_part1\\{i}')
