import os
folders_path = "C:/PythonProjects/git_test/LearnPython2021/100DaysOfPython" #input("Ender folder dirctory:")
folders_name ="Day-" #input("Enter folder name:")
folders_number = int(input("Enter folders number that you what to create :"))
os.chdir(folders_path)

for i in range (folders_number):
    try:
        os.mkdir(f"{folders_name}{i}")
    except:
        print(f"Can't create folder{folders_name}{i}")

