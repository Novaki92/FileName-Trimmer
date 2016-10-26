import os 

head = input("Enter beginning of file to be trimmed: ")
tail = input("Enter end of file to be trimmed (Do not include file etension) : ")
ext = input("Enter the file extension (.exe, .avi, .jpg, etc...): ")

if ext == "":
	ext = ".txt"

if "." not in ext:
	ext = "." + ext

for filename in os.listdir("."):
	if filename.endswith(ext):
		if filename.startswith(head):
			os.rename(filename, filename[len(head):])

for filename in os.listdir("."):
	if filename.endswith(ext):
		if filename.endswith(tail + ext):
			try:
				os.rename(filename, filename[:-len(tail + ext)])
			except FileNotFoundError:
				print("Tried to create blank file name...")
				break;

for filename in os.listdir("."):
		if "." not in filename:
			os.rename(filename, filename + ext)	

for filename in os.listdir("."):
	if filename.endswith(ext):
		print(filename)

input("Press any key to exit...")


