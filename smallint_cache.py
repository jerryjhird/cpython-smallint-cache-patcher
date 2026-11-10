# patches cpythons cached small int objects in place
# -5 to 256

import ctypes
import struct

_HEADER_SIZE = 3 * ctypes.sizeof(ctypes.c_ssize_t)
_DIGIT_BITS = 30  # PyLong_SHIFT
_DIGIT_MASK = (1 << _DIGIT_BITS) - 1
_DIGIT_SIZE = 4 

def _digit_addr(target):
    return id(target) + _HEADER_SIZE

def patch_smallint(target, new_value):
    addr = _digit_addr(target)
    ctypes.memmove(addr, struct.pack("=I", new_value), _DIGIT_SIZE)
