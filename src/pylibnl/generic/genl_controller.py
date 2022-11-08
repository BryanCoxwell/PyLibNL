from pylibnl.core import NL_SOCK_PTR
from pylibnl.executor import GenericExecutor
from ctypes import c_int, c_wchar_p, create_string_buffer, byref
from logging import getLogger

log = getLogger(__name__)

genl_api = GenericExecutor()

def genl_ctrl_resolve(sk: NL_SOCK_PTR, name: str) -> int:
    """ Resolves a Generic Netlink family name to numeric identifier. """
    buf = create_string_buffer(name.encode("ascii"))
    return genl_api.exec('genl_ctrl_resolve', c_int, sk, byref(buf))

def genl_ctrl_resolve_grp(
        sk: NL_SOCK_PTR, 
        family_name: str, 
        grp_name: str) -> int:
    """ Resolves a Generic Netlink family group name to numeric identifier. """
    return genl_api.exec('genl_ctrl_resolve_grp', c_int, sk, family_name, grp_name)