from pylibnl.executor import CoreExecutor
from pylibnl.core.nl_types import NLATTR_PTR, NLA_POLICY_PTR, NL_MSG_PTR
from ctypes import pointer, c_wchar_p, c_uint32, c_int, c_char_p, c_ubyte, c_ulonglong, c_ushort, byref
from functools import partial
from logging import getLogger

log = getLogger(__name__)

libnl_api = CoreExecutor()

def nla_find(head: NLATTR_PTR, lngth: int, attrtype: int) -> NLATTR_PTR | None:
    """ 
    Finds an attribute in a stream of attributes. 
    Returns first attribute that matches attrtype, or None if none do. 
    """
    return libnl_api.exec('nla_find', NLATTR_PTR, head, lngth, attrtype)

def nla_parse(
        tb, 
        maxtype: int, 
        head: NLATTR_PTR, 
        lngth: int, 
        policy: NLA_POLICY_PTR) -> int:
    """ 
    Create attribute index based on a stream of attributes. 
    tb: pointer to an array of attributes to be filled out by the parser
    TODO: figure out the type annotations for tb
    maxtype: maximum attribute type expected
    lngth: length of attribute stream
    policy: attribute validation policy

    Returns 0 on success or a negative error code
    """
    return libnl_api.exec('nla_parse', c_int, tb, maxtype, head, lngth, policy)

def nla_parse_nested(tb, maxtype: int, nla: NLATTR_PTR, policy: NLA_POLICY_PTR):
    """ Create attribute index based on nested attributes. """
    return libnl_api.exec('nla_parse_nested', c_int, tb, maxtype, nla, policy)

def nla_put_nested(msg: NL_MSG_PTR, attrtype: int, nested: NL_MSG_PTR) -> c_int:
    """ 
    Adds nested attributes to a netlink message. 
    Takes the attributes found in nested and appends them to the message msg in
    a container of type attrtype. The nested message may not have a family specific header.
    Returns 0 on success or a negative error code.
    """
    return libnl_api.exec('nla_put_nested', c_int, msg, attrtype, nested)

def nla_next(nla: NLATTR_PTR, remaining: int) -> NLATTR_PTR:
    """ Return the next attribute in a stream of attributes. """
    return libnl_api.exec('nla_next', NLATTR_PTR, nla, remaining)

def nla_ok(nla: NLATTR_PTR, remaining: int) -> bool:
    """ Check if the attribute header and payload can be safely accessed. """
    return libnl_api.exec('nla_ok', c_int, nla, remaining)

def nla_type(nla: NLATTR_PTR) -> int:
    """ Returns the type of the attribute. """
    return libnl_api.exec('nla_type', c_int, nla)

def nla_for_each_attr(head, lngth, func, *args, **kwargs):
    pos = head
    remaining = pointer(c_int(lngth))
    while remaining.contents.value > 0:
        func(pos)
        pos = nla_next(pos, remaining)

def nla_get_base(func_name, return_type, nla: NLATTR_PTR):
    """ Partial function. """
    return libnl_api.exec(func_name, return_type, nla)

nla_get_u8      = partial(nla_get_base, 'nla_get_u8', c_ubyte)
nla_get_u16     = partial(nla_get_base, 'nla_get_u16', c_ushort)
nla_get_u32     = partial(nla_get_base, 'nla_get_u32', c_uint32)
nla_get_u64     = partial(nla_get_base, 'nla_get_u64', c_ulonglong)
nla_get_string  = partial(nla_get_base, 'nla_get_string', c_char_p)
nla_get_flag    = partial(nla_get_base, 'nla_get_flag', c_int)

def nla_put_base(func_name, attr_c_type, msg, attr_type, value):
    """ Partial function. """
    return libnl_api.exec(func_name, attr_c_type, msg, attr_type, value)

nla_put_u8      = partial(nla_put_base, 'nla_put_u8', c_ubyte)
nla_put_u16     = partial(nla_put_base, 'nla_put_u16', c_ushort)
nla_put_u32     = partial(nla_put_base, 'nla_put_u32', c_uint32)
nla_put_u64     = partial(nla_put_base, 'nla_put_u64', c_ulonglong)
nla_put_string  = partial(nla_put_base, 'nla_put_string', c_char_p)
nla_put_flag    = partial(nla_put_base, 'nla_put_flag', c_int)
