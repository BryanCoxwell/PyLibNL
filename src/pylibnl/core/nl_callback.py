from enum import IntEnum
from typing import Callable
from ctypes import c_uint32, c_int
from pylibnl.core.api import CoreAPI
from pylibnl.core.nl_types import NL_CB, NL_CB_PTR, NL_MSG, NL_MSG_PTR, SOCKADDR_NL_PTR, NLMSGERR_PTR

libnl_api = CoreAPI()

class NL_CB_KIND(IntEnum):
    DEFAULT       = 0 
    VERBOSE       = 1
    DEBUG         = 2
    CUSTOM        = 3

class NL_CB_TYPE(IntEnum):
    VALID         = 0
    FINISH        = 1
    OVERRUN       = 2
    SKIPPED       = 3
    ACK           = 4
    MSG_IN        = 5
    MSG_OUT       = 6
    INVALID       = 7
    SEQ_CHECK     = 8
    SEND_ACK      = 9
    DUMP_INTR     = 10

class NL_CB_ACTION(IntEnum):
    OK      = 0
    SKIP    = 1
    STOP    = 2

def nl_cb_alloc(kind: NL_CB_KIND) -> NL_CB_PTR:
    """ Calculates the size of a netlink message based on payload length. """
    return libnl_api.exec('nl_cb_alloc', NL_CB_PTR, kind)

def nl_cb_clone(orig: NL_CB_PTR) -> NL_CB_PTR:
    """ Clone an existing callback handle. """
    return libnl_api.exec('nl_cb_clone', NL_CB_PTR, orig)

def nl_cb_active_type(cb: NL_CB_PTR) -> NL_CB_TYPE:
    """ Obtain type of current active callback. """
    return libnl_api.exec('nl_cb_active_type', c_uint32, cb)

def nl_cb_set(
        cb: NL_CB_PTR, 
        cb_type: NL_CB_TYPE, 
        kind: NL_CB_KIND, 
        fn: Callable[[NL_MSG_PTR], int]) -> int:
    """ 
    Set up a callback. 
    fn must be a callable that takes a pointer to a Netlink Message as an argument
    and returns an integer. 

    TODO: This should also take an argument of type *void to be passed to fn by the caller,
    but doing so currently causes a segfault.
    """
    return libnl_api.exec('nl_cb_set', c_int, cb, cb_type, kind, fn)

def nl_cb_err(
        cb: NL_CB_PTR, 
        kind: NL_CB_KIND, 
        fn: Callable[[SOCKADDR_NL_PTR, NLMSGERR_PTR], int]) -> int:
    """ 
    Set up an error callback. 
    fn must be a callable that takes a pointer to a Netlink Message as an argument
    and returns an integer. 

    TODO: This should also take an argument of type *void to be passed to fn by the caller,
    but doing so currently causes a segfault.
    """
    return libnl_api.exec('nl_cb_set', c_int, cb, kind, fn)