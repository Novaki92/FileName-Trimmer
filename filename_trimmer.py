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
#gives some feedback whenever users attempts to create a blank file name
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
#print all files with ext to console
for filename in os.listdir("."):
	if filename.endswith(ext):
		print(filename)
#wait for user input to close
input("Press any key to exit...")

### NOTES ###
# Yes I know this probably isn't the most effect method but it works
# If you attempt to run all the code in on instance of 'for filename in os.listdir("."):' you will encounter errors
# I tried that already and basically the filename changes and then it can't find the file to do the next step
# I also like the idea of it doing one step at a time in case I expand the code later
# This code is also supposed to be easy to read for programming newcomers / that's why I commented so extensively
# I know you get it but not everyone does. Make like an Interpreter and just ignore them.
### END ### 
