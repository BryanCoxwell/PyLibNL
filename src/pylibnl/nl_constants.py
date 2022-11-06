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