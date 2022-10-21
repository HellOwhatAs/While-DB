import WhileDB as wd
wd.update_globals({"n1":1234,"n2":5678})
wd.load_program("""
addr=malloc(16);
*addr=n1;
*(addr+8)=n2
""")
addr=wd.get_globals()["addr"]
wd.clear_globals()
del wd

import ctypes
val1=ctypes.cast(addr,ctypes.POINTER(ctypes.c_longlong)).contents.value
val2=ctypes.cast(addr+8,ctypes.POINTER(ctypes.c_longlong)).contents.value
print(val1, val2)
