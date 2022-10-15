from typing import Dict
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
def get_globals()->Dict[str,int]:
    """
    return global variables.
    """
def update_globals(_globals:Dict[str,int])->None:
    """
    update global variables.
    """
def clear_globals()->None:
    """
    delete all global variables.
    """
def to_end()->None:
    """
    execute the loaded program to end.
    """