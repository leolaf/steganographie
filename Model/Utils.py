from PIL import Image

SIZE_STORAGE = 16 # in byte

def get_bit(number: int, index: int):
    return (number>>index)&1

def msg_to_bytearray(msg):
    ascii_values = [ord(letter) for letter in msg]
    bits = []
    for value in ascii_values:
        for i in range(8):
            bits.append(get_bit(value,i))
    return bits

def bytearray_to_int(ba):
    ba.reverse()
    res = 0
    for bit in ba:
        res = res<<1
        res |= bit
    return res

def bytearray_to_chr(ba):
    return chr(bytearray_to_int(ba))

def bytearray_to_msg(ba):
    res = ""
    for i in range(0,len(ba),8):
        res += bytearray_to_chr(ba[i:i+8])
    return res

def int_to_bytearray(nb,size):
    bits = []
    for i in range(size):
        bits.append(get_bit(nb,i))
    return bits

def write_msg_size(msg_size: int, pixels: list, width: int, height: int):
    for i in range(0, SIZE_STORAGE, 3):
        idxPixel = i//3
        r, g, b, a = pixels[idxPixel%width, idxPixel//width]
        r = (r&254) | get_bit(msg_size,i)
        g = (g&254) | get_bit(msg_size,i+1)
        b = (b&254) | get_bit(msg_size,i+2)
        pixels[idxPixel%width, idxPixel//width] = r, g, b, a
    

def hide_msg(msg: str, initial_img_path: str, target_img_path: str):
    msg_size = len(msg) 
    img = open_img(initial_img_path)
    pixels = img.load()
    width, height = img.size
    
    # TODO verify image can contain msg
    
    bits_to_write = int_to_bytearray(msg_size, SIZE_STORAGE) + msg_to_bytearray(msg)
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

def find_msg(img_path:str):
    img = open_img(img_path)
    pixels = img.load()
    width, height = img.size

    msg_size_bits = []
    for i in range(0,SIZE_STORAGE,3):
        idxPixel = i//3
        r, g, b, a = pixels[idxPixel%width, idxPixel//width]
        msg_size_bits.append(r&1)
        msg_size_bits.append(g&1)
        msg_size_bits.append(b&1)

    msg_bits = []
    if(SIZE_STORAGE % 3 > 0):
        # Store overflow in msg_bits 
        msg_bits = msg_size_bits[-(SIZE_STORAGE % 3):]
        # Only keep wanted bits
        msg_size_bits[:-(SIZE_STORAGE % 3)]
    
    msg_size = bytearray_to_int(msg_size_bits)

    msg_size -= len(msg_bits)

    # TODO from here it certainly doesn't work
    firstPixel = (SIZE_STORAGE//3 + 1) * 3
    last_pixel = SIZE_STORAGE+msg_size

    for i in range(firstPixel,last_pixel,3):
        idxPixel = i//3
        r, g, b, a = pixels[idxPixel%width, idxPixel//width]
        msg_size_bits.append(r&1)
        if (i+1) < SIZE_STORAGE+msg_size:
            msg_size_bits.append(g&1)
        if (i+2) < SIZE_STORAGE+msg_size:
            msg_size_bits.append(b&1)

def open_img(path: str):
    return Image.open(path)