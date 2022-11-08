from typing import TypeAlias, TYPE_CHECKING
from ctypes import (
    Structure, c_ushort, c_uint, c_int, c_size_t, c_void_p, c_wchar_p, POINTER, _Pointer, CFUNCTYPE, Array
)

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

class NLATTR(Structure):
    """
    Reference:
    https://github.com/thom311/libnl/blob/cbafad9ddf24caef5230fef715d34f0539603be0/include/linux-private/linux/netlink.h#L206
    """
    ...

class NLA_POLICY(Structure):
    """
    Reference:
    https://github.com/thom311/libnl/blob/cbafad9ddf24caef5230fef715d34f0539603be0/include/netlink/attr.h#L63
    """
    ...

NL_RECVMSG_MSG_CB_T = CFUNCTYPE(c_int, POINTER(NL_MSG))
NL_RECVMSG_ERR_CB_T = CFUNCTYPE(c_int, POINTER(SOCKADDR_NL), POINTER(NLMSGERR))

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

NLATTR._fields_ = [
        ('nla_len', c_ushort),
        ('nla_type', c_ushort),
    ]

NLA_POLICY._fields_ = [
        ('type', c_uint),
        ('minlen', c_uint),
        ('maxlen', c_uint),
    ]

"""
MyPy and the ctypes lib have different ideas about what 
pointer types should look like. This makes them both happy.
"""
if TYPE_CHECKING:
    NL_SOCK_PTR: TypeAlias      = _Pointer[NL_SOCK]
    NL_CB_PTR: TypeAlias        = _Pointer[NL_CB]
    NL_MSG_PTR: TypeAlias       = _Pointer[NL_MSG]
    NLMSG_HDR_PTR: TypeAlias    = _Pointer[NLMSG_HDR]
    SOCKADDR_NL_PTR: TypeAlias  = _Pointer[SOCKADDR_NL]
    NLMSGERR_PTR: TypeAlias     = _Pointer[NLMSGERR]
    NLATTR_PTR: TypeAlias       = _Pointer[NLATTR]
    UCRED_PTR: TypeAlias        = _Pointer[UCRED]
    NLA_POLICY_PTR: TypeAlias   = _Pointer[NLA_POLICY]
    C_INT_PTR: TypeAlias        = _Pointer[c_int]
    C_WCHAR_P_PTR: TypeAlias    = _Pointer[c_wchar_p]
else:
    NL_SOCK_PTR                 = POINTER(NL_SOCK)
    NL_CB_PTR                   = POINTER(NL_SOCK)
    NL_MSG_PTR                  = POINTER(NL_MSG)
    NLMSG_HDR_PTR               = POINTER(NLMSG_HDR)
    SOCKADDR_NL_PTR             = POINTER(SOCKADDR_NL)
    NLMSGERR_PTR                = POINTER(NLMSGERR)
    NLATTR_PTR                  = POINTER(NLATTR)
    UCRED_PTR                   = POINTER(UCRED)
    NLA_POLICY_PTR              = POINTER(NLA_POLICY)
    C_INT_PTR                   = POINTER(c_int)
    C_WCHAR_P_PTR               = POINTER(c_wchar_p)