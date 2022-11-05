from ctypes import pointer
from ctypes import POINTER
from ctypes import _Pointer
from typing import TypeAlias, TYPE_CHECKING
from pylibnl.nl_types import NL_SOCK
from pylibnl.api import API
from pylibnl.nl_types import NL_RECVMSG_MSG_CB_T
from pylibnl.nl_types import NL_RECVMSG_ERR_CB_T
libnl_api = API()

if TYPE_CHECKING:
    NL_SOCK_PTR: TypeAlias = _Pointer[NL_SOCK]
else:
    NL_SOCK_PTR = POINTER(NL_SOCK)


def add_groups(*args):
    if args[-1] != 0:
        args = (*args, 0)
    print(*args)