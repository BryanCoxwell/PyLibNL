from typing import Callable
from ctypes import c_int, c_uint, c_uint32, c_size_t, c_void_p, c_wchar_p
from pylibnl.core.nl_callback import NL_CB_KIND, NL_CB_TYPE
from pylibnl.executor import CoreExecutor
from pylibnl.core.nl_types import (
    SOCKADDR_NL, SOCKADDR_NL_PTR, NL_SOCK, NL_SOCK_PTR, NL_MSG, NL_MSG_PTR, NL_CB, NL_CB_PTR, 
    NLMSGERR, NLMSGERR_PTR, UCRED_PTR, C_WCHAR_P_PTR, NL_RECVMSG_MSG_CB_T, NL_RECVMSG_ERR_CB_T
)
from logging import getLogger

log = getLogger(__name__)

NL_AUTO_PORT    = 0
NL_AUTO_SEQ     = 0

libnl_api = CoreExecutor()

def nl_socket_alloc() -> NL_SOCK_PTR:
    """ Allocate a new Netlink socket. """
    return libnl_api.exec('nl_socket_alloc', NL_SOCK_PTR)    

def nl_socket_alloc_cb(cb: NL_CB_PTR): 
    """ Allocate a new Netlink socket with custom callbacks. """
    return libnl_api.exec('nl_socket_alloc_cb', NL_SOCK_PTR, cb)

def nl_socket_free(sk: NL_SOCK_PTR) -> None:
    """ Free a Netlink socket. """
    libnl_api.exec('nl_socket_free', None, sk)

def nl_socket_disable_seq_check(sk: NL_SOCK_PTR) -> None:
    """ Disable sequence number checking. """
    libnl_api.exec('nl_socket_disable_seq_check', None, sk)

def nl_socket_use_seq(sk: NL_SOCK_PTR) -> int:
    """ Use next sequence number. """
    return libnl_api.exec('nl_socket_use_seq', c_uint, sk)

def nl_socket_disable_auto_ack(sk: NL_SOCK_PTR) -> None:
    """ Disable automatic request for ACKs. """
    libnl_api.exec('nl_socket_disable_auto_ack', None, sk)

def nl_socket_enable_auto_ack(sk: NL_SOCK_PTR) -> None:
    """ Enables requesting ACKs automatically. """
    libnl_api.exec('nl_socket_enable_auto_ack', None, sk)

def nl_socket_set_local_port(sk: NL_SOCK_PTR, port: int) -> None:
    """ Sets local socket port ID. """
    libnl_api.exec('nl_socket_set_local_port', None, sk, port)

def nl_socket_add_memberships(sk: NL_SOCK_PTR, *args: int) -> c_int:
    """ 
    Join multicast groups.
    Per the docs, the list of memberships must be terminated with a 0.
    If it isn't, we add one here:
    """
    if args[-1] != 0:
        args = (*args, 0)
    return libnl_api.exec('nl_socket_add_memberships', c_int, sk, *args)

def nl_socket_drop_memberships(sk: NL_SOCK_PTR, *args: int) -> int:
    """ Leave multicast groups. """
    return libnl_api.exec('nl_socket_drop_memberships', c_int, sk, *args)

def nl_socket_get_fd(sk: NL_SOCK_PTR) -> int:
    """ Get socket file descriptor. """
    return libnl_api.exec('nl_socket_get_fd', c_int, sk)

def nl_socket_set_nonblocking(sk: NL_SOCK_PTR) -> int:
    """ Set file descriptor of socket to a non-blocking state. """
    return libnl_api.exec('nl_socket_set_nonblocking', c_int, sk)

def nl_socket_enable_msg_peek(sk: NL_SOCK_PTR) -> None:
    """ Enable use of MSG_PEEK when reading from socket. """
    libnl_api.exec('nl_socket_enable_msg_peek', None, sk)

def nl_socket_disable_msg_peek(sk: NL_SOCK_PTR) -> None:
    """ Disable use of MSG_PEEK when reading from socket. """
    libnl_api.exec('nl_socket_disable_msg_peek', None, sk)

def nl_socket_modify_cb(
        sk: NL_SOCK_PTR,
        cb_type: NL_CB_TYPE, 
        cb_kind: NL_CB_KIND, 
        fn: Callable[[NL_MSG_PTR], int]) -> int:
    """ 
    Modify the callback handler associated with the socket. 
    fn must be a callable that takes a pointer to a Netlink Message as an argument
    and returns an integer. 

    TODO: This should also take an argument of type *void to be passed to fn by the caller,
    but doing so currently causes a segfault.
    """
    cfunc = NL_RECVMSG_MSG_CB_T(fn)
    return libnl_api.exec('nl_socket_modify_cb', c_int, sk, cb_type, cb_kind, cfunc, None)

def nl_socket_modify_err_cb(
        sk: NL_SOCK_PTR,
        cb_type: c_uint, 
        cb_kind: c_uint, 
        fn: Callable[[SOCKADDR_NL_PTR, NLMSGERR_PTR], int]) -> int:
    """ 
    Modify the error callback handler associated with the socket. 
    fn must be a callable that takes a pointer to a Netlink Message as an argument
    and returns an integer. 

    TODO: This should also take an argument of type *void to be passed to fn by the caller,
    but doing so currently causes a segfault.
    """
    cfunc = NL_RECVMSG_ERR_CB_T(fn)
    return libnl_api.exec('nl_socket_modify_err_cb', c_int, sk, cb_type, cb_kind, cfunc)

def nl_socket_set_buffer_size(
        sk: NL_SOCK_PTR,
        rxbuf: int, 
        txbuf: int) -> int:
    """ Set socket buffer size of the netlink socket. """
    return libnl_api.exec('nl_socket_set_buffer_size', c_int, sk, rxbuf, txbuf)

def nl_socket_set_msg_buf_size(sk: NL_SOCK_PTR, bufsize: int) -> int:
    """ Set default message buffer size of netlink socket. """
    return libnl_api.exec('nl_socket_set_msg_buf_size', c_int, sk, bufsize)

def nl_socket_get_msg_buf_size(sk: NL_SOCK_PTR) -> int:
    """ Get default message buffer size of netlink socket. """
    return libnl_api.exec('nl_socket_set_msg_buf_size', c_size_t, sk)

def nl_socket_set_passcred(sk: NL_SOCK_PTR, state: int) -> int:
    """ 
    Enable/disable credential passing on netlink socket. 
    State value: 0 - disabled, 1 - enabled
    """
    return libnl_api.exec('nl_socket_set_passcred', c_int, sk, state)

def nl_socket_recv_pktinfo(sk: NL_SOCK_PTR, state: int) -> int:
    """ 
    Enable/disable reception of additional packet information on netlink socket. 
    State value: 0 - disabled, 1 - enabled
    """
    return libnl_api.exec('nl_socket_recv_pktinfo', c_int, sk, state)

def nl_connect(sk: NL_SOCK_PTR, nl_family: int) -> int:
    """ Bind the socket. """
    return libnl_api.exec('nl_connect', c_int, sk, nl_family)

def nl_close(sk: NL_SOCK_PTR) -> None:
    """ Closes the socket. """
    libnl_api.exec('nl_close', None, sk)

def nl_sendto(
        sk: NL_SOCK_PTR, 
        buf: str, 
        size: c_size_t) -> int:
    """ 
    Sends raw data over the netlink socket.
    The message is addressed to the peer as specified in the socket by either the 
    nl_socket_set_peer_port() or nl_socket_Set_peer_groups() functions.
    Returns the number of bytes sent or a negative error code.
    """
    buf_ptr = c_wchar_p(buf)
    return libnl_api.exec('nl_sendto', c_int, sk, buf_ptr, size)

def nl_sendmsg():
    """ 
    Sends raw data over the netlink socket.
    The message is addressed to the peer as specified in the socket by either the 
    nl_socket_set_peer_port() or nl_socket_Set_peer_groups() functions.
    Returns the number of bytes sent or a negative error code.
    """
    raise NotImplementedError("Not implemented. Consider using nl_send() instead.")

def nl_send(sk: NL_SOCK_PTR, msg: NL_MSG_PTR) -> int:
    """ Transmit a Netlink Message. """
    return libnl_api.exec('nl_send', c_int, sk, msg)

def nl_complete_msg(sk: NL_SOCK_PTR, msg: NL_MSG_PTR) -> None:
    """ Finalizes a Netlink message by completing the message with desirable flags and values depending on the socket configuration. """
    libnl_api.exec('nl_complete_message', None, sk, msg)

def nl_send_auto(sk: NL_SOCK_PTR, msg: NL_MSG_PTR) -> int:
    """ Finalizes msg using nl_complete_msg() then sends it. """
    return libnl_api.exec('nl_send_auto', c_int, sk, msg)

def nl_send_sync(sk: NL_SOCK_PTR, msg: NL_MSG_PTR) -> int:
    """ Passes the message to nl_send_auto() and waits for the ACK or error message. """
    return libnl_api.exec('nl_send_sync', c_int, sk, msg)

def nl_send_simple(
        sk: NL_SOCK_PTR, 
        msg_type: int,
        flags: int,
        buf: str, 
        size: int) -> int:
    """ Passes the message to nl_send_auto() and waits for the ACK or error message. """
    buf_ptr = c_wchar_p(buf)
    return libnl_api.exec('nl_send_sync', c_int, sk, msg_type, flags, buf_ptr, size)

def nl_recv(
        sk: NL_SOCK_PTR,
        peer_address: SOCKADDR_NL_PTR,
        buf: C_WCHAR_P_PTR,
        creds: UCRED_PTR) -> int:
    """ 
    Receives data from a connected NL socket using recvmsg().
    Returns the number of bytes read.
    This function blocks until data is available unless nl_socket_set_nonblocking() has been called
    Returns number of bytes read, 0 on EOF, 0 on no data event, or a negative error code
    """
    return libnl_api.exec('nl_recv', c_int, sk, peer_address, buf, creds)

def nl_recvmsgs_report(sk: NL_SOCK_PTR, cb: NL_CB_PTR) -> int:
    """ 
    Receive a set of messages from a netlink socket and report parsed messages.
    Returns the number of parsed messages or a negative error code.
    """
    return libnl_api.exec('nl_recvmsgs_report', c_int, sk, cb)

def nl_recvmsgs(sk: NL_SOCK_PTR, cb: NL_CB_PTR) -> int:
    """ 
    Receive a set of messages from a netlink socket. 
    Returns 0 on success or a negative error code
    """
    return libnl_api.exec('nl_recvmsgs', c_int, sk, cb)

def nl_recvmsgs_default(sk: NL_SOCK_PTR) -> int:
    """ Receive a set of message from a netlink socket using handlers in NL_SOCK. """
    return libnl_api.exec('nl_recvmsgs_default', c_int, sk)

def nl_wait_for_ack(sk: NL_SOCK_PTR) -> int:
    """ Wait for ACK. Returns 0 on success or a negative error code. """
    return libnl_api.exec('nl_wait_for_ack', c_int, sk)

def nl_pickup():
    """ Pickup netlink answer, parse it, and return the parsed object. """
    raise NotImplementedError

def nl_auto_complete():
    """ Deprecated: Please use nl_complete_msg() """
    return NotImplementedError("Deprecated: please use nl_complete_msg()")

def nl_send_auto_complete():
    """ Deprecated: Please use nl_send_auto() """
    return NotImplementedError("Deprecated: please use nl_send_auto()")