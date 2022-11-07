from ctypes import CDLL
from ctypes.util import find_library
from logging import getLogger

log = getLogger(__name__)

class API():
    def __init__(self, lib_name: str):
        """ 
        The find_library function should just return None if the shared lib
        isn't found, but sometimes it raises a FileNotFound error.
        """
        try:
            self.libpath = find_library(lib_name)
            if not self.libpath:
                raise FileNotFoundError
        except FileNotFoundError:
            raise SystemExit(f"Library not found: lib{lib_name}.so. Exiting...")
        self.lib = CDLL(self.libpath)

    def exec(
            self, 
            func, 
            return_type, 
            *args,
            **kwargs):
        """ Sets the return type of func and calls the function. """
        fn = self.lib[func]
        fn.restype = return_type
        return fn(*args, **kwargs)

class CoreAPI(API):
    def __init__(self):
        super().__init__("nl-3")

class GenericAPI(API):
    def __init__(self):
        super().__init__("nl-genl-3")