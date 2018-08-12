#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jpiye
#
# Created:     12/08/2018
# Copyright:   (c) jpiye 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    #onemillionlittlefibers()
    whileloop()

def onemillionlittlefibers():
    for jonq in range(0, 1000000):
        print(jonq)


def whileloop():
    x = 1
    while x <= 100:
        print (x)
        x = x + 1

if __name__ == '__main__':
    main()
