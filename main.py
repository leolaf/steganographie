import argparse
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5

from Model import Steganography 

KEYPATH = "keys/"
KEY_SIZE = 2048
RSA_PRIVATE_KEY="private.pem"
RSA_PUBLIC_KEY="public.pem"

def rsa_key_gen(bits=KEY_SIZE, privatekey_path=RSA_PRIVATE_KEY, pubkey_path=RSA_PUBLIC_KEY):
    private_key = RSA.generate(bits)
    with open(KEYPATH + privatekey_path, "wb") as privkey_file:
        privkey_file.write(private_key.export_key())
    with open(KEYPATH + pubkey_path, "wb") as pubkey_file:
        pubkey_file.write(private_key.publickey().export_key())

if __name__ == "__main__" :
    parser = argparse.ArgumentParser(description='###  Steganography tool  ###')
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-H", "--hide", action="store_true", help = "Hide messsage in image -i <image> -o <output> -m <message>")
    group.add_argument("-F", "--find", action="store_true", help = "Find messsage in image -i <image>")
    parser.add_argument("-i", "--image", dest="image", help="Image to hide or find message in -i <image>")
    parser.add_argument("-m", "--message", dest="msg", help="Message to hide in image -i <image> -o <output> -m <message>")
    parser.add_argument("-o", "--output", dest="output", help="Output image -i <image> -o <output> -m <message>")
    parser.add_argument("-k", "--keys", dest="keys", action="store_true", help="Generate RSA keys -pub <public key file> -priv <private key file>")
    parser.add_argument("-pub", "--public", dest="pubkey", help="Public key file -pub <public key file>")
    parser.add_argument("-priv", "--private", dest="privkey", help="Private key file -priv <private key file>")
    parser.add_argument("-s", "--sign", dest="sign", action="store_true", help="Sign message -i <image> -priv <private key file>")
    parser.add_argument("-sig", "--signature", dest="signature", help="Signature of message")
    parser.add_argument("-V", "--verify", dest="verify", action="store_true", help="Verify message -i <image> -sig <signature> -pub <public key file>")
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
    if args.keys:
        if args.pubkey is None or args.privkey is None:
            rsa_key_gen()
        else:
            rsa_key_gen(privatekey_path=args.privkey, pubkey_path=args.pubkey)
    if args.sign:
        if args.image is None or args.privkey is None:
            parser.error("Missing arguments")
        with open(KEYPATH + args.privkey, "rb") as privkey_file:
            privkey = RSA.import_key(privkey_file.read())
        with open(args.image, "rb") as image_file:
            image = image_file.read()
        hash = SHA256.new(image)
        signer = PKCS1_v1_5.new(privkey)
        signed_hash = signer.sign(hash)
        print(signed_hash.hex())
    if args.verify:
        if args.image is None or args.pubkey is None or args.signature is None:
            parser.error("Missing arguments")
        with open(KEYPATH + args.pubkey, "rb") as pubkey_file:
            pubkey = RSA.import_key(pubkey_file.read())
        h = SHA256.new()
        h.update(open(args.image, "rb").read())
        verifier = PKCS1_v1_5.new(pubkey)
        signature = bytes(args.signature.encode("utf-8"))
        print(verifier.verify(h, signature))