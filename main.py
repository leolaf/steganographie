import sys
from Model import hide_msg,find_msg

def help():
    print("pas comme ça")

if __name__ == "__main__" :
    argv = sys.argv[1:]
    argc = len(argv)
    if(argc == 0):
        help()
    if(argc == 1):
        print(find_msg(argv[0]))
    if(argc == 3):
        hide_msg(argv[0],argv[1],argv[2])