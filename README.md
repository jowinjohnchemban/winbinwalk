# Install and use binwalk in Windows

This is a redirect program to pass the arguments along with the command to execute the binwalk.
eg: If user input "binwalk file.bin" as command via cmd this program will make it execute as "python binwalk file.bin"
Thus making it possible to execute easily.


binwalk repo : www.github.com/ReFirmLabs/binwalk

                                                
   Coded By : Jowin John Chemban                
                                                
   GitHub   : www.github.com/jowinjohnchemban/
   
   Twitter  : www.twitter.com/jowinchemban/
   
   Donate   : www.paypal.me/jowinjohnchemban


Steps to setup...
 
 
Install Python 2.7 for Windows from www.python.org

Install python-lzma module

Download binwalk zip from binwalk repo at GitHub

Extract and Open the directory and Open cmd there.

Enter "python setup.py install", binwalk will be installed.


Now, Download the binwalk.py script from here and keep it in a isolated folder at Desktop.

Open cmd in the above folder and enter "pip install pyinstaller", pyinstaller get installed.

Enter "pyinstaller --onefile binwalk.py", This will create an executable (.exe) of binwalk.py

Navigate to dist folder inside current folder where you can find the executable file, Copy it to "C:\Windows\System32\"

Now you can remove the previously created folder at Desktop.
 
 





  Open cmd from the directory with the file to decrypt and run it as usual.
  
  
  DISCLAIMER : This is just a modification to the orginal binwalk and all the credits regarding binwalk goes to the orginal developers.
               Any doubts regarding binwalk visit the orginal repo.
               
