from Crypto.Util.number import * # bytes_to_long
from sympy import symbols, solve, Eq # import *



def create_variables():
    x, y, z = symbols('x y z', integer=True)
    return x, y, z


def solve_system(v1, v2, v3, v4):
    x, y, z = create_variables()
    equations = [
        Eq(x**3 + z**2 + y, v1),
        Eq(y**3 + x**2 + z, v2),
        Eq(z**3 + y**2 + x, v3),
        Eq(x + y + z, v4),
    ]
    solutions = solve(equations, (x, y, z), dict=True)
    return solutions[0] if solutions else None

def get_flag(sols):
    x, y, z = create_variables()
    parts = [long_to_bytes(int(sols[var])) for var in [x, y, z]]
    return b''.join(parts)

def load_values():
    with open('output.txt') as f:
        data = f.read()
    return {
        'v1' : int(data.split('v1 = ')[1].split('\n')[0]),
        'v2' : int(data.split('v2 = ')[1].split('\n')[0]),
        'v3' : int(data.split('v3 = ')[1].split('\n')[0]),
        'v4' : int(data.split('v4 = ')[1])
    }

def pwn():
    values = load_values()
    solutions = solve_system(**values)
    if solutions:
        flag = get_flag(solutions)
        print(flag.decode())
    else:
        print("No se encontraron soluciones válidas")

if __name__ == '__main__':
    pwn()