import sys
from Model import hide_msg

def help():
    print("pas comme ça")

if __name__ == "__main__" :
    argv = sys.argv[1:]
    argc = len(argv)
    if(argc == 0):
        help()
    else:
        hide_msg(argv[0],argv[1],argv[2])