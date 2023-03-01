import sys
from Model import Steganography

def help():
    print("pas comme ça")

if __name__ == "__main__" :
    argv = sys.argv[1:]
    argc = len(argv)
    if(argc == 0):
        help()
    if(argc == 1):
        print(Steganography.find_msg(argv[0]))
    if(argc == 3):
        Steganography.hide_msg(argv[0],argv[1],argv[2])