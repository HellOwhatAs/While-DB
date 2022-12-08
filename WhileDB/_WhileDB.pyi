from typing import Dict, Tuple, Iterable, Iterator, overload, ItemsView, KeysView, ValuesView

class Unordered_MapStringInt:
    def __bool__(self) -> bool:
        "Check whether the map is nonempty"
    @overload
    def __contains__(self, arg0: str) -> bool:...
    @overload
    def __contains__(self, arg0: object) -> bool:...
    def __delitem__(self, arg0: str) -> None:...
    def __getitem__(self, arg0: str) -> int:...
    def __init__(self) -> None:...
    def __iter__(self) -> Iterator:...
    def __len__(self) -> int:...
    def __repr__(self) -> str:
        "Return the canonical string representation of this map."
    def __setitem__(self, arg0: str, arg1: int) -> None:...
    def items(self) -> ItemsView[Unordered_MapStringInt]:...
    def keys(self) -> KeysView[Unordered_MapStringInt]:...
    def values(self) -> ValuesView[Unordered_MapStringInt]:...

    def clear(self)->None:
        "Remove all items."
    @overload
    def update(self, __m: Dict[str, int], **kwargs: int) -> None: ...
    @overload
    def update(self, __m: Iterable[Tuple[str, int]], **kwargs: int) -> None: ...
    @overload
    def update(self, **kwargs: int) -> None: ...


def load_program(src: str, exec_to_end:bool=True)->None:
    """
    load the While-DB code. (and exec it to end if `exec_to_end` is True) 
    ### Parameters:
    ------
    `src`: str
        the While-DB code

    `exec_to_end`: bool
        if True then execute the code to end  

        else do not execute
    ### Return:
    ------
    `None`
    """
def end()->bool:
    """
    return `True` if the loaded program can step foward\n
    otherwise `False`.
    ### Return:
    ------
    `bool`
    """
def step()->None:
    """
    step foward the loaded program.
    """
def Globals()->Unordered_MapStringInt:
    """
    return global variables by reference.
    """
def to_end()->None:
    """
    execute the loaded program to end.
    """