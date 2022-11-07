from enum import IntEnum

class NetlinkFamily(IntEnum):
    ROUTE           = 0
    UNUSED          = 1
    USERSOCK        = 2
    FIREWALL        = 3
    SOCK_DIAG       = 4
    NFLOG           = 5
    XFRM            = 6
    SELINUX         = 7
    ISCSI           = 8
    AUDIT           = 9
    FIB_LOOKUP      = 10
    CONNECTOR       = 11
    NETFILTER       = 12
    IP6_FW          = 13
    DNRTMSG         = 14
    KOBJECT_UEVENT  = 15
    GENERIC         = 16
    SCSITRANSPORT   = 18
    ECRYPTFS        = 19
    RDMA            = 20
    CRYPTO          = 21
    SMC             = 22

class Error(IntEnum):
    SUCCESS                         = 0
    FAILURE                         = -1
    INTERRUPTED                     = -2
    BAD_SOCK                        = -3
    TRY_AGAIN                       = -4
    NO_MEMORY                       = -5
    OBJECT_EXISTS                   = -6
    INVALID_INPUT                   = -7
    INPUT_OUT_OF_RANGE              = -8
    MESSAGE_SIZE_INSUFFICIENT       = -9
    OPERATION_NOT_SUPPORTED         = -10
    OBJECT_NOT_FOUND                = -11
    ATTRIBUTE_NOT_AVAILABLE         = -12
    ADDRESS_FAMILY_MISMATCH         = -13
    SEQUENCE_MISMATCH               = -14
    MESSAGE_OVERFLOW                = -15
    MESSAGE_TRUNCATED               = -16
    INVALID_ADDRESS                 = -17
    SOURCE_ROUTING_NOT_SUPPORTED    = -18
    MESSAGE_TOO_SHORT               = -19
    MESSAGE_TYPE_NOT_SUPPORTED      = -20
    OBJECT_MISMATCH                 = -21
    INVALID_CACHE_TYPE              = -22
    OBJECT_BUSY                     = -23
    PROTOCOL_MISMATCH               = -24
    NO_ACCESS                       = -25
    OPERATION_NOT_PERMITTED         = -26
    UNABLE_TO_OPEN_PKTLOC_FILE      = -27
    UNABLE_TO_PARSE_OBJECT          = -28
    NO_SUCH_DEVICE                  = -29
    IMMUTABLE_ATTRIBUTE             = -30
    DUMP_INCONSISTENCY_DETECTED     = -31
