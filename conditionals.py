#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jpiye
#
# Created:     19/08/2018
# Copyright:   (c) jpiye 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    name ="mary"
    name = raw_input("enter your name")
    password = raw_input("enter your password")

    if name == "mary" or password == "catfood":
        print ("hello mary")
    else:
        print ("name or password mismatch")

if __name__ == '__main__':
    main()