from pylibnl.api import API
from ctypes import c_int, c_void_p
from pylibnl.nl_types import C_INT_PTR, NL_MSG, NL_MSG_PTR, NLMSG_HDR, NLMSG_HDR_PTR, NLATTR, NLATTR_PTR
from logging import getLogger

log = getLogger(__name__)

libnl_api = API()

def nlmsg_alloc() -> NL_MSG_PTR:
    """ Allocate a new netlink message with the default maximum payload size. """
    return libnl_api.exec('nlmsg_alloc', NL_MSG_PTR)

def nlmsg_size(payload: c_int) -> c_int:
    """ Calculates the size of a netlink message based on payload length. """
    return libnl_api.exec('nlmsg_size', c_int, payload)

def nlmsg_total_size(payload: c_int) -> c_int:
    """ Calculates the size of a netlink message including padding based on payload length. """
    return libnl_api.exec('nlmsg_total_size', c_int, payload)

def nlmsg_padlen(payload: c_int) -> c_int:
    """ Size of padding that needs to be added at end of message. """
    return libnl_api.exec('nlmsg_padlen', c_int, payload)

def nlmsg_data(nlh: NLMSG_HDR_PTR) -> c_void_p:
    """ Returns a pointer to message payload. """
    return libnl_api.exec('nlmsg_data', c_void_p, nlh)

def nlmsg_datalen(nlh: NLMSG_HDR_PTR) -> c_int:
    """ Returns the length of message payload. """
    return libnl_api.exec('nlmsg_datalen', c_int, nlh)

def nlmsg_attrdata(nlh: NLMSG_HDR_PTR, hdrlen: c_int) -> NLATTR_PTR:
    """ Returns a pointer to the head of attribute data. """
    return libnl_api.exec('nlmsg_attrdata', NLATTR_PTR, nlh, hdrlen)

def nlmsg_attrlen(nlh: NLMSG_HDR_PTR, hdrlen: c_int) -> c_int:
    """ Returns the length of attributes data. """
    return libnl_api.exec('nlmsg_attrlen', c_int, nlh, hdrlen)

def nlmsg_ok(nlh: NLMSG_HDR_PTR, remaining: int) -> c_int:
    """ Check if the Netlink message fits into a buffer's remaining bytes. """
    return libnl_api.exec('nlmsg_ok', c_int, nlh, remaining)

def nlmsg_next(nlh: NLMSG_HDR_PTR, remaining: C_INT_PTR) -> NLMSG_HDR_PTR:
    """ Return the next message in a message stream. """
    return libnl_api.exec('nlmsg_next', NLMSG_HDR_PTR, nlh, remaining)

def nl_msg_dump(nl_msg: NL_MSG_PTR, fd: int) -> None:
    """ Dump a message in human readable form to the file descriptor fd. """
    libnl_api.exec('nl_msg_dump', None, nl_msg, fd)