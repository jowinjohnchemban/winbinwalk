import os
import sys

strl = ''.join(sys.argv[1:])
command = "python C:\\Python27\\Scripts\\binwalk "+strl
os.system(command)


# This is a redirect program to pass the arguments along with the command to
# execute the binwalk.
# eg: If user input "binwalk file.bin" as command via cmd
#     this program will make it execute as "python binwalk file.bin"
# Thus make it possible to execute easily.


# binwalk repo : https://github.com/ReFirmLabs/binwalk

##################################################
#                                                #
#   Coded By : Jowin John Chemban                #
#                                                #
#   GitHub   : www.github.com/jowinjohnchemban/  #
#   Twitter  : www.twitter.com/jowinchemban/     #
#                                                #
#   Donate   : www.paypal.me/jowinjohnchemban    #
#                                                #
##################################################
