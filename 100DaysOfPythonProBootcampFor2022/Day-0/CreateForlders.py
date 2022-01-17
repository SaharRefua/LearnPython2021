import os
folders_path = "C:/PythonProjects/LearnPython2021/100DaysOfPythonProBootcampFor2022" #input("Ender folder dirctory:")
folders_name = input("Ender folder name:")
folders_number = int(input("Ender folders number that you what to create :"))
os.chdir(folders_path)

for i in range (folders_number):
    try :
        os.mkdir(f"{folders_name}{i}")
    except:
        print(f"Can't create folder{folders_name}{i}")

