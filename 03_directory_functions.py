import os

folder = "demo_folder"
file_name = "demo_folder/sample.txt"

print("Current directory:", os.getcwd())
os.mkdir(folder)
print("Directory created:", os.path.exists(folder))
print("Is directory:", os.path.isdir(folder))
print("Joined path:", os.path.join(folder, "sample.txt"))

file = open(file_name, "w")
file.write("Directory handling example")
file.close()

print("Is file:", os.path.isfile(file_name))
print("Directory contents:", os.listdir(folder))
os.rename(file_name, "demo_folder/new_sample.txt")
print("Renamed file exists:", os.path.exists("demo_folder/new_sample.txt"))
os.remove("demo_folder/new_sample.txt")
os.rmdir(folder)
print("Directory removed:", not os.path.exists(folder))
