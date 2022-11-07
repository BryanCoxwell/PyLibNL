from ctypes import Structure, c_ubyte, c_ushort, _Pointer, POINTER
from typing import TYPE_CHECKING, TypeAlias

class GENLMSGHDR(Structure):
    """
    Reference:
    https://github.com/thom311/libnl/blob/cbafad9ddf24caef5230fef715d34f0539603be0/include/linux-private/linux/genetlink.h#L13
    """
    ...


GENLMSGHDR._fields_ = [
        ('cmd', c_ubyte),
        ('version', c_ubyte),
        ('reserved', c_ushort),
    ]


if TYPE_CHECKING:
    GENLMSGHDR_PTR: TypeAlias   = _Pointer[GENLMSGHDR]
else:
    GENLMSGHDR_PTR              = POINTER(GENLMSGHDR)
   