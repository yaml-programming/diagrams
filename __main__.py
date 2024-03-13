import src
import pathlib
import sys
from discopy.frobenius import Id, Box, Ty

from files import path_diagram
from src.data.nat import nat_f

def argv_diagrams():
    paths = iter(sys.argv[1:])
    for path in map(pathlib.Path, paths):
        yield path_diagram(path)


f = nat_f
ds = argv_diagrams()
d = Id().tensor(*ds)
print(f(d)())
