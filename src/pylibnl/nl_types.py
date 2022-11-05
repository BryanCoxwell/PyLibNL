from ctypes import Structure
from ctypes import c_ushort
from ctypes import c_uint
from ctypes import c_int
from ctypes import c_size_t
from ctypes import c_void_p
from ctypes import POINTER
from ctypes import CFUNCTYPE
from typing import NewType
from typing import Protocol
from enum import IntEnum

"""
This file defines libnl types as objects that inherit from the ctype library's Structure class. 
All classes are forward declared to avoid interdependencies causing issues with the order
in which they're defined. 
"""

class UCRED(Structure):
    """
    Reference:
    https://docs.huihoo.com/doxygen/linux/kernel/3.7/structucred.html
    """
    ...

class SOCKADDR_NL(Structure):
    """
    Reference: 
    https://github.com/thom311/libnl/blob/cbafad9ddf24caef5230fef715d34f0539603be0/include/linux-private/linux/netlink.h#L37
    """
    ...

class NLMSG_HDR(Structure):
    """
    Reference:
    https://github.com/thom311/libnl/blob/cbafad9ddf24caef5230fef715d34f0539603be0/include/linux-private/linux/netlink.h#L44
    """
    ...

class NL_MSG(Structure):
    """
    Reference:
    https://github.com/thom311/libnl/blob/cbafad9ddf24caef5230fef715d34f0539603be0/include/netlink-private/types.h#L144
    """
    ...

class NL_CB(Structure):
    """
    Reference:
    https://github.com/thom311/libnl/blob/cbafad9ddf24caef5230fef715d34f0539603be0/include/netlink-private/types.h#L48
    """
    ...

class NL_SOCK(Structure):
    """
    Reference:
    https://github.com/thom311/libnl/blob/cbafad9ddf24caef5230fef715d34f0539603be0/include/netlink-private/types.h#L78
    """
    ...

class NLMSGERR(Structure):
    """
    Reference:
    https://github.com/thom311/libnl/blob/cbafad9ddf24caef5230fef715d34f0539603be0/include/linux-private/linux/netlink.h#L109
    """
    ...

NL_RECVMSG_MSG_CB_T = CFUNCTYPE(c_int, POINTER(NL_MSG), c_void_p)
NL_RECVMSG_ERR_CB_T = CFUNCTYPE(c_int, POINTER(SOCKADDR_NL), c_void_p)

UCRED._fields_ = [
        ('pid', c_uint),
        ('uid', c_uint),
        ('gid', c_uint),
    ]

SOCKADDR_NL._fields_ = [
        ("nl_family", c_ushort),
        ("nl_pad", c_ushort),
        ("nl_pid", c_uint),
        ("nl_groups", c_uint),
    ]

NLMSG_HDR._fields_ = [
        ('nlmsg_len', c_uint),
        ('nlmsg_type', c_ushort),
        ('nlmsg_flags', c_ushort),
        ('nlmsg_seq', c_uint),
        ('nlmsg_pid', c_uint),
    ]

NL_MSG._fields_ = [
        ('nm_protocol', c_int),
        ('nm_flags', c_int),
        ('nm_src', SOCKADDR_NL),
        ('nm_dst', SOCKADDR_NL),
        ('nm_cred', UCRED),
        ('nm_nlh', POINTER(NLMSG_HDR)),
        ('nm_size', c_size_t),
        ('nm_refcount', c_int),
    ]

NL_CB._fields_ = [
        ('cb_set', NL_RECVMSG_MSG_CB_T),
        ('cb_args', c_void_p),
        ('cb_err', NL_RECVMSG_ERR_CB_T),
        ('cb_err_arg', c_void_p),
        ('cb_recvmsgs_ow', c_int),
        ('cb_recv_ow', c_int),
        ('cb_send_ow', c_int),
        ('cb_refcnt', c_int),
        ('cb_active', c_uint),
    ]

NL_SOCK._fields_ = [
        ('s_local', SOCKADDR_NL),
        ('s_peer', SOCKADDR_NL),
        ('s_fd', c_int),
        ('s_proto', c_int),
        ('s_seq_next', c_uint),
        ('s_seq_expect', c_uint),
        ('s_flags', c_int),
        ('s_cb', POINTER(NL_CB)),
        ('s_bufsize', c_size_t),
    ]

NLMSGERR._fields_ = [
        ('error', c_int),
        ('msg', NL_MSG),
    ]
