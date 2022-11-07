from pylibnl.core.api import GenericAPI
from pylibnl.core.nl_types import NL_SOCK_PTR
from pylibnl.core.nl_socket import nl_connect
from pylibnl.core.nl_constants import NetlinkFamily
from ctypes import c_int

genl_api = GenericAPI()

def genl_connect(sk: NL_SOCK_PTR) -> int:
    """ Connect to a Generic Netlink socket. """
    return nl_connect(sk, NetlinkFamily.GENERIC)

def genl_send_simple(
        sk: NL_SOCK_PTR,
        family: int,
        cmd: int,
        version: int,
        flags: int) -> int:
    return genl_api.exec('genl_send_simple', c_int, sk, family, cmd, version, flags)