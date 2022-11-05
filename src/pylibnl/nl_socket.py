from typing import TypeAlias
from typing import Callable
from typing import Optional
from typing import TYPE_CHECKING
from ctypes import c_int
from ctypes import c_uint
from ctypes import c_uint32
from ctypes import c_size_t
from ctypes import c_void_p
from ctypes import _Pointer
from ctypes import POINTER
from pylibnl.api import API
from pylibnl.nl_types import SOCKADDR_NL
from pylibnl.nl_types import NLMSGERR
from pylibnl.nl_types import NL_SOCK
from pylibnl.nl_types import NL_CB
from pylibnl.nl_types import NL_MSG
from pylibnl.nl_types import NL_RECVMSG_MSG_CB_T
from pylibnl.nl_types import NL_RECVMSG_ERR_CB_T

import logging
log = logging.getLogger(__name__)

"""
MyPy and the ctypes lib have different ideas about what 
pointer types should look like. This makes them both happy.
"""
if TYPE_CHECKING:
    NL_SOCK_PTR: TypeAlias      = _Pointer[NL_SOCK]
    NL_CB_PTR: TypeAlias        = _Pointer[NL_CB]
    NL_MSG_PTR: TypeAlias       = _Pointer[NL_MSG]
    SOCKADDR_NL_PTR: TypeAlias  = _Pointer[SOCKADDR_NL]
    NLMSGERR_PTR: TypeAlias     = _Pointer[NLMSGERR]
else:
    NL_SOCK_PTR                 = POINTER(NL_SOCK)
    NL_CB_PTR                   = POINTER(NL_SOCK)
    NL_MSG_PTR                  = POINTER(NL_MSG)
    SOCKADDR_NL_PTR             = POINTER(SOCKADDR_NL)
    NLMSGERR_PTR                = POINTER(NLMSGERR)

libnl_api = API()

def alloc() -> NL_SOCK_PTR:
    """ Allocate a new Netlink socket. """
    return libnl_api('nl_socket_alloc', NL_SOCK_PTR)    

def alloc_cb(cb: NL_CB_PTR): 
    """ Allocate a new Netlink socket with custom callbacks. """
    return libnl_api('nl_socket_alloc_cb', NL_SOCK_PTR, cb)

def free(sk: NL_SOCK_PTR) -> None:
    """ Free a Netlink socket. """
    libnl_api('nl_socket_free', None, sk)

def disable_seq_check(sk: NL_SOCK_PTR) -> None:
    """ Disable sequence number checking. """
    libnl_api('nl_socket_disable_seq_check', None, sk)

def use_seq(sk: NL_SOCK_PTR) -> c_uint:
    """ Use next sequence number. """
    return libnl_api('nl_socket_use_seq', c_uint, sk)

def disable_auto_ack(sk: NL_SOCK_PTR) -> None:
    """ Disable automatic request for ACKs. """
    libnl_api('nl_socket_disable_auto_ack', None, sk)

def enable_auto_ack(sk: NL_SOCK_PTR) -> None:
    """ Enables requesting ACKs automatically. """
    libnl_api('nl_socket_enable_auto_ack', None, sk)

def set_local_port(sk: NL_SOCK_PTR, port: c_uint32) -> None:
    """ Sets local socket port ID. """
    libnl_api('nl_socket_set_local_port', None, sk, port)

def add_memberships(sk: NL_SOCK_PTR, *args: c_int) -> c_int:
    """ 
    Join multicast groups.
    Per the docs, the list of memberships must be terminated with a 0.
    If it isn't, we add one here:
    """
    if args[-1] != 0:
        args = (*args, 0)
    return libnl_api('nl_socket_add_memberships', c_int, sk, *args)

def drop_memberships(sk: NL_SOCK_PTR, *args: c_int) -> c_int:
    """ Leave multicast groups. """
    return libnl_api('nl_socket_drop_memberships', c_int, sk, *args)

def get_fd(sk: NL_SOCK_PTR) -> c_int:
    """ Get socket file descriptor. """
    return libnl_api('nl_socket_get_fd', c_int, sk)

def set_nonblocking(sk: NL_SOCK_PTR) -> c_int:
    """ Set file descriptor of socket to a non-blocking state. """
    return libnl_api('nl_socket_set_nonblocking', c_int, sk)

def enable_msg_peek(sk: NL_SOCK_PTR) -> None:
    """ Enable use of MSG_PEEK when reading from socket. """
    libnl_api('nl_socket_enable_msg_peek', None, sk)

def disable_msg_peek(sk: NL_SOCK_PTR) -> None:
    """ Disable use of MSG_PEEK when reading from socket. """
    libnl_api('nl_socket_disable_msg_peek', None, sk)

def modify_cb(
        sk: NL_SOCK_PTR,
        cb_type: c_uint, 
        cb_kind: c_uint, 
        fn: Callable[[NL_MSG_PTR, Optional[c_void_p]], c_int], 
        arg: c_void_p) -> c_int:
    """ Modify the callback handler associated with the socket. """
    cfunc = NL_RECVMSG_MSG_CB_T(fn)
    return libnl_api('nl_socket_modify_cb', c_int, sk, cb_type, cb_kind, cfunc, arg)

def modify_err_cb(
        sk: NL_SOCK_PTR,
        cb_type: c_uint, 
        cb_kind: c_uint, 
        fn: Callable[[SOCKADDR_NL_PTR, NLMSGERR_PTR, Optional[c_void_p]], c_int], 
        arg: c_void_p = None) -> c_int:
    """ Modify the error callback handler associated with the socket. """
    cfunc = NL_RECVMSG_ERR_CB_T(fn)
    return libnl_api('nl_socket_modify_err_cb', c_int, sk, cb_type, cb_kind, cfunc, arg)

def set_buffer_size(
        sk: NL_SOCK_PTR,
        rxbuf: c_int, 
        txbuf: c_int) -> c_int:
    """ Set socket buffer size of the netlink socket. """
    return libnl_api('nl_socket_set_buffer_size', c_int, sk, rxbuf, txbuf)

def set_msg_buf_size(sk: NL_SOCK_PTR, bufsize: c_size_t) -> c_int:
    """ Set default message buffer size of netlink socket. """
    return libnl_api('nl_socket_set_msg_buf_size', c_int, sk, bufsize)

def get_msg_buf_size(sk: NL_SOCK_PTR) -> c_size_t:
    """ Get default message buffer size of netlink socket. """
    return libnl_api('nl_socket_set_msg_buf_size', c_size_t, sk)

def set_passcred(sk: NL_SOCK_PTR, state: c_int) -> c_int:
    """ 
    Enable/disable credential passing on netlink socket. 
    State value: 0 - disabled, 1 - enabled
    """
    return libnl_api('nl_socket_set_passcred', c_int, sk, state)

def recv_pktinfo(sk: NL_SOCK_PTR, state: c_int) -> c_int:
    """ 
    Enable/disable reception of additional packet information on netlink socket. 
    State value: 0 - disabled, 1 - enabled
    """
    return libnl_api('nl_socket_recv_pktinfo', c_int, sk, state)

def connect(sk: NL_SOCK_PTR, nl_family: c_int) -> c_int:
    """ Bind the socket. """
    return libnl_api('nl_connect', c_int, sk, nl_family)
