
class BinaryOperations:

    def __init__(self) -> None:
        pass

    @classmethod
    def get_bit(number: int, index: int):
        return (number>>index)&1

    @classmethod
    def msg_to_bytearray(msg):
        ascii_values = [ord(letter) for letter in msg]
        bits = []
        for value in ascii_values:
            for i in range(8):
                bits.append(BinaryOperations.get_bit(value,i))
        return bits

    @classmethod
    def bytearray_to_int(ba):
        ba.reverse()
        res = 0
        for bit in ba:
            res = res<<1
            res |= bit
        return res

    @classmethod
    def bytearray_to_chr(ba):
        return chr(BinaryOperations.bytearray_to_int(ba))

    @classmethod
    def bytearray_to_msg(ba):
        res = ""
        for i in range(0,len(ba),8):
            res += BinaryOperations.bytearray_to_chr(ba[i:i+8])
        return res

    @classmethod
    def int_to_bytearray(nb,size):
        bits = []
        for i in range(size):
            bits.append(BinaryOperations.get_bit(nb,i))
        return bits