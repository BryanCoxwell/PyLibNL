from pylibnl.api import API
from ctypes import c_int
from ctypes import c_void_p
from ctypes import POINTER

NL_AUTO_PORT    = 0
NL_AUTO_SEQ     = 0


libnl_api = API()

def size(self, payload: c_int) -> c_int:
    """ Calculates the size of a netlink message based on payload length. """
    return libnl_api('nlmsg_size', c_int, payload)

def total_size(self, payload: c_int) -> c_int:
    """ Calculates the size of a netlink message including padding based on payload length. """
    return libnl_api('nlmsg_total_size', c_int, payload)

def padlen(self, payload: c_int) -> c_int:
    """ Size of padding that needs to be added at end of message. """
    return libnl_api('nlmsg_padlen', c_int, payload)

def data(self, nlh: POINTER(NLMSG_HDR)) -> c_void_p:
    """ Returns a pointer to message payload. """
    return libnl_api('nlmsg_data', c_void_p, nlh)

def datalen(self, nlh: POINTER(NLMSG_HDR)) -> c_int:
    """ Returns the length of message payload. """
    return libnl_api('nlmsg_datalen', c_int, nlh)

def attrdata(self, nlh: POINTER(NLMSG_HDR), hdrlen: c_int) -> POINTER(NLATTR):
    """ Returns a pointer to the head of attribute data. """
    return libnl_api('nlmsg_attrdata', POINTER(NLATTR), nlh, hdrlen)

def attrlen(self, nlh: POINTER(NLMSG_HDR), hdrlen: c_int) -> c_int:
    """ Returns the length of attributes data. """
    return libnl_api('nlmsg_attrlen', c_int, nlh, hdrlen)

def ok(self, nlh: POINTER(NLMSG_HDR), remaining: int) -> c_int:
    """ Check if the Netlink message fits into a buffer's remaining bytes. """
    return libnl_api('nlmsg_ok', c_int, nlh, remaining)

def next(self, nlh: POINTER(NLMSG_HDR), remaining: POINTER(c_int)) -> POINTER(NLMSG_HDR):
    """ Return the next message in a message stream. """
    return libnl_api('nlmsg_next', POINTER(NLMSG_HDR), nlh, remaining)



