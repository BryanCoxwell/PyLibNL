from ctypes import CDLL
from ctypes.util import find_library
from typing import Callable

import logging
log = logging.getLogger(__name__)

LIBNAME_SHORT = "nl-3"
LIBNAME_FULL = "libnl-3.so"

class API():
    def __init__(self):
        """ 
        The find_library function should just return None if the shared lib
        isn't found, but sometimes it raises a FileNotFound error.
        """
        try:
            self.libpath = find_library(LIBNAME_SHORT)
        except FileNotFoundError:
            log.warning(f"Library not found by name: {self.libpath}. Attempting with filename {LIBNAME_FULL}...")
            self.libpath = LIBNAME_FULL
        try:
            self.lib = CDLL(self.libpath)
        except OSError:
            raise SystemExit("Unable to find or open libnl-3. Exiting...")

    def __call__(self, func, return_type, *args):
        fn = self.lib[func]
        fn.restype = return_type
        return fn(*args)