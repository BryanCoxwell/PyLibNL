from enum import IntEnum, IntFlag

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

class NetlinkError(IntEnum):
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

class NetlinkMessageFlag(IntFlag):
    """
    Defines the flags that can be sent with Netlink Messages.
    https://github.com/torvalds/linux/blob/master/include/uapi/linux/netlink.h
    """

    """ Standard Flag Bits """
    REQUEST         = 1         # Request message
    MULTI           = 2         # Multipart message, terminated by NLMSG_DONE
    ACK             = 4         # Request for an acknowledgement on success
    ECHO            = 8         # Echo this request
    DUMP_INTR       = 16        # Dump was inconsistent due to sequence change
    DUMP_FILTERED   = 32        # Dump was filtered as requested

    """ Additional flag bits for GET requests. """
    ROOT            = 256       # Return the complete table instead of a single entry.
    MATCH           = 512       # Return all entries matching criteria. Not implemented.
    ATOMIC          = 1024      # Return an atomic snapshot of the table
    DUMP            = 768       # Convenience macro for (ROOT | MATCH)

    """ Additional flag bits for NEW requests. """
    REPLACE         = 256       # Replace existing matching object
    EXCL            = 512       # Don't replace object if it exists
    CREATE          = 1024      # Create object if it doesn't already exist
    APPEND          = 2048      # Add to the end of the object list

    """ Additional flag bits for DELETE requests. """
    NONREC          = 256       # Do not delete recursively
    BULK            = 512       # Delete multiple objects

    """ Additional flag bits for ACK messages. """
    CAPPED          = 256       # Request was capped
    ACK_TLVS        = 512       # Extended ACK TVLs were included