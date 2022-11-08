from pylibnl.core import NLMSG_HDR_PTR, NLA_POLICY_PTR, NLATTR_PTR, NL_MSG_PTR
from pylibnl.generic.genl_types import GENLMSGHDR_PTR
from pylibnl.executor import GenericExecutor
from ctypes import c_int, c_void_p, c_uint32
from logging import getLogger

log = getLogger(__name__)

genl_api = GenericExecutor()

def genlmsg_valid_hdr(
        nlh: NLMSG_HDR_PTR,
        hdrlen: int) -> int:
    """ 
    Validate a Generic Netlink message header. 
    Returns a positive integer if valid, 0 if invalid
    """
    return genl_api.exec('genlmsg_valid_hdr', c_int, nlh, hdrlen)

def genlmsg_validate(
        nlh: NLMSG_HDR_PTR,
        hdrlen: int,
        maxtype: int,
        nla_policy: NLA_POLICY_PTR) -> int:
    """ 
    Validate a Generic Netlink message header including attributes. 
    Returns 0 on success or a negative error code.
    """
    return genl_api.exec('genlmsg_validate', c_int, nlh, hdrlen, maxtype, nla_policy)

def genlmsg_parse(
        nlh: NLMSG_HDR_PTR,
        hdrlen: int,
        tb,
        maxtype: int,
        nla_policy: NLA_POLICY_PTR) -> int:
    """
    Parse a Generic Netlink message including attributes.
    Returns 0 on success or a negative error code.
    TODO: Figure out the type annotation for tb. tb is a pointer to an array which 
    the parsed attributes will be stored in, but there doesn't seem to be a straightforward
    way to annotate that without knowing the length of the array ahead of time. 
    """
    return genl_api.exec('genlmsg_parse', c_int, nlh, hdrlen, tb, maxtype, nla_policy)

def genlmsg_hdr(nlh: NLMSG_HDR_PTR) -> GENLMSGHDR_PTR:
    """ Returns a pointer to the Generic Netlink header. """
    return genl_api.exec('genlmsg_hdr', GENLMSGHDR_PTR, nlh)

def genlmsg_len(gnlh: GENLMSGHDR_PTR) -> int:
    """ Return length of message payload including the user header. """
    return genl_api.exec('genlmsg_len', c_int, gnlh)

def genlmsg_user_hdr(gnlh: GENLMSGHDR_PTR) -> c_void_p:
    """ Returns a pointer to the user header. """
    return genl_api.exec('genlmsg_user_hdr', c_void_p, gnlh)

def genlmsg_user_data(gnlh: GENLMSGHDR_PTR, hdrlen: int) -> c_void_p:
    """ Returns a pointer to the user data. """
    return genl_api.exec('genlmsg_user_data', c_void_p, gnlh, hdrlen)

def genlmsg_user_datalen(gnlh: GENLMSGHDR_PTR, hdrlen: int) -> int:
    """ Returns length of the user data. """
    return genl_api.exec('genlmsg_user_datalen', c_int, gnlh, hdrlen)

def genlmsg_attrdata(gnlh: GENLMSGHDR_PTR, hdrlen: int) -> NLATTR_PTR:
    """ Returns a pointer to message attributes. """
    return genl_api.exec('genlmsg_attrdata', NLATTR_PTR, gnlh, hdrlen)

def genlmsg_attrlen(gnlh: GENLMSGHDR_PTR, hdrlen: int) -> int:
    """ Returns length of the message attributes. """
    return genl_api.exec('genlmsg_attrlen', c_int, gnlh, hdrlen)

def genlmsg_put(
        msg: NL_MSG_PTR,
        port: int,
        seq: int,
        family: int,
        hdrlen: int,
        flags: int,
        cmd: int,
        version: int = 1) -> c_void_p:
    """ 
    Add Generic Netlink headers to a Netlink message.
    Returns a pointer to the user header.
    """
    return genl_api.exec('genlmsg_put', c_void_p, msg, port, seq, family, hdrlen, flags, cmd, version)

def genlmsg_data(gnlh: GENLMSGHDR_PTR) -> c_void_p:
    """ Returns a pointer to the message payload. """
    return genl_api.exec('genlmsg_data', c_void_p, gnlh)