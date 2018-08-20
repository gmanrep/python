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

    if name != "dwight" or password == "catfood":
        print ("thank god you're not dwight")
    else:
        print ("go away dwight..")

if __name__ == '__main__':
    main()