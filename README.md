# FileName Trimmer
Trims the beginning and end of filenames for multiple files. 

This program was created entirely because of the excessive amounts of digital media with redundant file names. 

Check the [Wiki](https://github.com/Novaki92/FileName-Trimmer/wiki) for a quick visual tutorial. 
************************************************************
- For Windows Users [Download](https://github.com/Novaki92/FileName-Trimmer/raw/master/dist/filename_trimmer.exe)

        1) .exe is in dist folder if download link isn't working

        2) place into directory you wish to trim file names

        3) follow prompts
        
        4) delete program - this is intended to be disposable software

    
- For Linux Users

        1) You're on Linux...I mean python is like the defualt man...figure it out 

        2) But seriously just make sure you have python 3 and run from terminal like all other py scripts

        3) This script hasn't been tested on any Linux OS as of yet but it should run fine

        4) Oh and same as windows...Make sure filename_trimmer.py is in the folder you want to trim files
    
- For Mac Users

        1) Make sure you have Python installed on your machine by opening terminal and typing 'python'
        
        2) Copy filename_trimmer.py into the folder you wish to work in
        
        3) Right click and then select Open With then select IDLE 
        
        4) Click IDLE then go to Run and then select Run Module (or press Function + F5) 
        
        5) Follow prompts then close IDLE 
        
        
- For Programmers

        1) If you want an exe you'll need to download PyInstaller from http://www.pyinstaller.org/ 
        
        1.5) Or better yet just run 'pip install pyinstaller' in terminal/cmd

        2) Go to the correct directory that your .py script is in (in terminal/cmd)

        3) I personally run 'pyinstaller --onefile filename_trimmer.py' for sake of simplicity but you can use something else if you want

- FAQ:

        Q: Do I need to include a period when entering file extension?
        A: It's up to your preference...FileName Trimmer works fine with or without the period in the extension
        
        
        Q: Can I use this on files with numbers at the beginning? 
        A: If it's all the same number. Otherwise it wont work. 
        
        
        Q: What happens if I don't enter anything?
        A: If you don't enter anything into the head or tail then nothing happens to whichever end you didn't put any text. 
        If you don't enter anything into the file extension then it defaults to .txt.
