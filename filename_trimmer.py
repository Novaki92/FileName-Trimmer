import os 
#user input for variables
head = input("Enter beginning of file to be trimmed: ")
tail = input("Enter end of file to be trimmed (Do not include file etension) : ")
ext = input("Enter the file extension (.exe, .avi, .jpg, etc...): ")
#prevent errors by assigning .txt as default extension
if ext == "":
	ext = ".txt"
#prevent errors by checking for period in file extension
#adds period to start if none present
if "." not in ext:
	ext = "." + ext
#cycle through all the files in the directory
#if file is the same extension as user input and starts with head trim the head
for filename in os.listdir("."):
	if filename.endswith(ext):
		if filename.startswith(head):
			os.rename(filename, filename[len(head):])
#cycle through again
#if filename ends with tail trim tail 
#have to trim with extension here
#Gives some feedback whenever users attempts to create a blank file name
for filename in os.listdir("."):
	if filename.endswith(ext):
		if filename.endswith(tail + ext):
			try:
				os.rename(filename, filename[:-len(tail + ext)])
			except FileNotFoundError:
				print("Tried to create blank file name...")
				break;
#check for files that do not contain a period since we just removed extensions
#append file name with extension
for filename in os.listdir("."):
		if "." not in filename:
			os.rename(filename, filename + ext)	
#print all files to console
for filename in os.listdir("."):
	if filename.endswith(ext):
		print(filename)
#wait for user input to close
input("Press any key to exit...")