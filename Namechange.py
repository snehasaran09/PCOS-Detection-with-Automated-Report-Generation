import os
path = os.chdir(
    "C:\\Users\\Sneha Saravanan\\Desktop\\College Work\\B.Tech-Year3\\6th Sem\\Capstone\\PCOS\\Datasets\\Combined Dataset\\Proper")
i = 1
for file in os.listdir(path):
    new_file_name = "image_{}.jpg".format(i)
    os.rename(file, new_file_name)
    i = i+1
