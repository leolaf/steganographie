import sys
import argparse
from Model import Steganography 

if __name__ == "__main__" :
    parser = argparse.ArgumentParser(description='###  Steganography tool  ###')
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-H", "--hide", action="store_true", help = "Hide messsage in image -i <image> -o <output> -m <message>")
    group.add_argument("-F", "--find", action="store_true", help = "Find messsage in image -i <image>")
    parser.add_argument("-i", "--image", dest="image", help="Image to hide or find message in -i <image>")
    parser.add_argument("-m", "--message", dest="msg", help="Message to hide in image -i <image> -o <output> -m <message>")
    parser.add_argument("-o", "--output", dest="output", help="Output image -i <image> -o <output> -m <message>")
    args = parser.parse_args()

    if args.hide:
        if args.image is None or args.msg is None:
            parser.error("Missing arguments")
        out = args.output
        if out is None:
            out = "output.png"
        Steganography.hide_msg(args.msg, args.image, args.output)
    if args.find:
        if args.image is None:
            parser.error("Missing arguments")
        print(Steganography.find_msg(args.image))