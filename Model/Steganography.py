from PIL import Image
import BinaryOperations

class Steganography:

    SIZE_STORAGE = 16

    def __init__(self) -> None:
        pass

    @classmethod
    def open_img(path: str):
        return Image.open(path)

    @classmethod
    def hide_msg(msg: str, initial_img_path: str, target_img_path: str):
        msg_size = len(msg) 
        img = Steganography.open_img(initial_img_path)
        pixels = img.load()
        width = img.width
        
        # TODO verify image can contain msg
        
        bits_to_write = BinaryOperations.int_to_bytearray(msg_size, Steganography.SIZE_STORAGE) + BinaryOperations.msg_to_bytearray(msg)
        nb_bits_to_write = len(bits_to_write)
        for i in range(0,nb_bits_to_write, 3):
            idxPixel = i//3
            r, g, b, a = pixels[idxPixel%width, idxPixel//width]
            r = (r&254) | bits_to_write[i]
            if (i+1) < nb_bits_to_write:
                g = (g&254) | bits_to_write[i+1]
            if (i+2) < nb_bits_to_write:
                b = (b&254) | bits_to_write[i+2]
            pixels[idxPixel%width, idxPixel//width] = r, g, b, a
    
        img.save(target_img_path)
    
    @classmethod
    def find_msg(img_path:str):
        img = Steganography.open_img(img_path)
        pixels = img.load()
        width = img.width

        msg_size_bits = []
        msg_bits = []
        for i in range(0,Steganography.SIZE_STORAGE,3):
            idxPixel = i//3
            r, g, b, a = pixels[idxPixel%width, idxPixel//width]
            msg_size_bits.append(r&1)
            if(i+1 < Steganography.SIZE_STORAGE):
                msg_size_bits.append(g&1)
            else:
                msg_bits.append(g&1)
            if(i+2 < Steganography.SIZE_STORAGE):
                msg_size_bits.append(b&1)
            else:
                msg_bits.append(b&1)

        msg_size = BinaryOperations.bytearray_to_int(msg_size_bits)
        
        firstPixel = Steganography.SIZE_STORAGE + len(msg_bits)
        assert(firstPixel%3 == 0)
        last_pixel = firstPixel + msg_size*8 - len(msg_bits)

        for i in range(firstPixel,last_pixel,3):
            idxPixel = i//3
            r, g, b, a = pixels[idxPixel%width, idxPixel//width]
            msg_bits.append(r&1)
            if (i+1) < last_pixel:
                msg_bits.append(g&1)
            if (i+2) < last_pixel:
                msg_bits.append(b&1)

        return BinaryOperations.bytearray_to_msg(msg_bits)