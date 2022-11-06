# PyLibNL

### **Note: This is a work in progress.**


PyLibNL is a Python implementation of the [Netlink Protocol Library Suite (libnl)](https://www.infradead.org/~tgr/libnl/). It uses Python's `ctypes` library to find, load, and call functions of the libnl shared libraries. 

Type names and function names and return types are kept the same as libnl except where they'd interfere with Python's reserved words/builtin functions. 

