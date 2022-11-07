import pytest
from ctypes import POINTER
from pylibnl.core.nl_callback import *
from pylibnl.core.nl_socket import *
from pylibnl.core.nl_types import *


def test_nl_socket_alloc():
    ptr = nl_socket_alloc()
    assert isinstance(ptr, NL_SOCK_PTR)

def test_nl_cb_alloc_default():
    ptr = nl_cb_alloc(NL_CB_KIND.DEFAULT)
    assert isinstance(ptr, NL_CB_PTR)

def test_nl_cb_alloc_verbose():
    ptr = nl_cb_alloc(NL_CB_KIND.VERBOSE)
    assert isinstance(ptr, NL_CB_PTR)

def test_nl_cb_alloc_debug():
    ptr = nl_cb_alloc(NL_CB_KIND.DEBUG)
    assert isinstance(ptr, NL_CB_PTR)

def test_nl_cb_alloc_custom():
    ptr = nl_cb_alloc(NL_CB_KIND.CUSTOM)
    assert isinstance(ptr, NL_CB_PTR)

def test_nl_socket_alloc_cb():
    cb_ptr = nl_cb_alloc(NL_CB_KIND.DEFAULT)
    sk_ptr = nl_socket_alloc_cb(cb_ptr)
    assert isinstance(sk_ptr, NL_SOCK_PTR)

def test_nl_socket_free():
    sk = nl_socket_alloc()
    nl_socket_free(sk)
    err = nl_connect(sk, 0)
    assert err < 0

def test_nl_socket_get_fd_before_connect():
    # socket should not have a file descriptor before calling nl_connect()
    sk = nl_socket_alloc()
    fd = nl_socket_get_fd(sk)
    assert fd < 0

def test_nl_socket_get_fd_after_connect():
    sk = nl_socket_alloc()
    nl_connect(sk, 0)
    fd = nl_socket_get_fd(sk)
    assert fd > 0