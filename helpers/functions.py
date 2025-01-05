import itertools
from collections import defaultdict

def read_file(dir, file):
    return open(dir + file,'r').read().splitlines()

def load(dir, day):
    return read_file(dir, "day{}.txt".format(day))
    
def mapl(fn, *args):
    return list(map(fn, *args))

def first(l): 
    return next(iter(l))

def is_unique(l):
    return len(set(l)) == len(l)

def is_prime(n):
    return n > 1 and all(n%i for i in itertools.islice(itertools.count(2), int(math.sqrt(n)-1)))

def sort(items):
    cast = ''.join if isinstance(items, str) else tuple 
    return cast(sorted(items))

def add(x,y):
    return map(sum, zip(x,y))

def mult(x, v):
    return [i*v for i in x]

def create_grid(puzzle_input, sep=""):
    grid = defaultdict(lambda: defaultdict(str))
    
    for r_idx, row in enumerate(puzzle_input.splitlines()):
        elems = row.split(sep) if sep else list(row)
        for c_idx, elem in enumerate(elems):
            grid[r_idx][c_idx] = elem
            
    return grid      
        