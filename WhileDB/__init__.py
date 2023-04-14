from typing import Dict, Iterable, Union, Tuple
from ._WhileDB import *

def _Unordered_MapStringInt_clear(self:Unordered_MapStringInt):
    keys=list(self.keys())
    for key in keys:self.__delitem__(key)
Unordered_MapStringInt.clear=_Unordered_MapStringInt_clear

def _Unordered_MapStringInt_update(self:Unordered_MapStringInt, args:Union[Dict[str, int], Iterable[Tuple[str, int]]]=None, **kwargs):
    if args != None:
        if hasattr(args, "items"):
            for k,v in args.items():
                self[k]=v
        else:
            for k,v in args:
                self[k]=v
    for k,v in kwargs.items():
        self[k]=v
Unordered_MapStringInt.update=_Unordered_MapStringInt_update