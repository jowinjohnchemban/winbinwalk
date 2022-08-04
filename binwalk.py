import os
import sys

strl = ''.join(sys.argv[1:])
command = 'python "C:\\Program Files\\Python37\\Scripts\\binwalk" ' + strl
os.system(command)

# This is a redirect program to pass the arguments along with the command to
# execute the binwalk.
# eg: If user input "binwalk file.bin" as command via cmd
#     this program will make it execute as "python binwalk file.bin"
# Thus make it possible to execute easily.

# ReFirmLabs binwalk repo : https://github.com/ReFirmLabs/binwalk
