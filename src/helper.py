from typing import List
from os import path

def read_filedata(filepath:str) -> str:
    if not path.isfile(filepath): raise Exception("File does not exist")
    line_arr: List[str] = []
    with  open(filepath, "r") as f:
        for line in f:
            line_arr.append(line)
    return "".join(line_arr)

def write_filedata(filepath:str, filedata:str) -> None:
    with  open(filepath, "w") as f:
        f.write(filedata)
