import WhileDB as wd
import ctypes, numpy as np
arr=np.array([2,3,5,7,11,13,17],dtype=np.int64)

addr=arr.ctypes.data_as(ctypes.c_void_p).value
wd.update_globals({"a": addr, "l":arr.shape[0]})
wd.load_program("""
i=0;
while i<l do{
    *(a+i*8)=(*(a+i*8))*(*(a+i*8));
    i=i+1
}
""")

print(arr)
