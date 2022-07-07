import sys
sys.setrecursionlimit(10 ** 6)

length = 9
ary = []
blank = []

def setBit(ary, x, y):
    # print("setBit", x, y)
    h_Bit = 0
    v_Bit = 0
    s_Bit = 0
    for i in range(y):
#       print("vertical", bin(v_Bit), bin(1 << ary[i][x]), ary[i][x])
        v_Bit |= (1 << ary[i][x])
#       print(bin(v_Bit))
    for i in range(x):
#       print("horizontal", bin(h_Bit), bin(1 << ary[y][i]), ary[y][i])
        h_Bit |= (1 << ary[y][i])
#       print(bin(h_Bit))
    for i in range(3):
        for k in range(3):
            #print(x, y, x-x%3+i, y-y%3+k, ary[x-x%3+i][y-y%3+k])
#       print("square", bin(s_Bit), bin(1 << ary[y // 3 * 3 + i][x // 3 * 3 + k]), ary[y // 3 * 3 + i][x // 3 * 3 + k])
            s_Bit |= (1 << ary[y - y % 3 + k][x - x % 3 + i])
#       print(bin(s_Bit))
    return h_Bit, v_Bit, s_Bit


def checkBit(h_Bit, v_Bit, s_Bit, posNum):
    # print ("checkBit", bin(h_Bit), bin(v_Bit), bin(s_Bit), bin(1 << posNum))
    # print (bin(h_Bit & (1 << posNum)), bin(v_Bit & (1 << posNum)), bin(s_Bit & (1 << posNum)))
    if h_Bit & (1 << posNum) != 0:
        return False
    if v_Bit & (1 << posNum) != 0:
        return False
    for k in range(3):
        if s_Bit & (1 << posNum) != 0:
            return False
    return True


def recursiveFillCell(ary, index):
    if index == len(blank):
        for i in range(9):
            print(*ary[i])
        exit(0)
    
    y, x = blank[index]
    h_Bit, v_Bit, s_Bit = setBit(ary, x, y)

    # print(index, x, y, bin(h_Bit), bin(v_Bit), bin(s_Bit))
    # for i in range(9):
    #    print(*ary[i])

    for i in range(1, 10):
        if(checkBit(h_Bit, v_Bit, s_Bit, int(i))):
            ary[y][x] = int(i)
            recursiveFillCell(ary, index + 1)
            ary[y][x] = 0


for i in range(length) :
    ary.append(list(map(int, sys.stdin.readline().rstrip().split())))

# for i in range(length) :
#     print(*ary[i])

for i in range(length):
    for j in range(9):
        if ary[i][j] == 0:
            blank.append((i, j))
# print(*blank)

recursiveFillCell(ary, 0)

# ************ Solution *******************************************************

sys.setrecursionlimit(10 ** 6)
def read_list_str(): return list(sys.stdin.readline().strip().split(' '))

def cross(aa: list, bb: list):
    return [a + b for a in aa for b in bb]


digits = '123456789'
rows = 'ABCDEFGHI'
cols = digits
squares = cross(rows, cols)
unitlist = ([cross(rows, c) for c in cols] +
            [cross(r, cols) for r in rows] +
            [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')])
units = dict((s, [u for u in unitlist if s in u])
             for s in squares)
peers = dict((s, set(sum(units[s], []))-set([s]))
             for s in squares)


def assign(values, s, d):
    other_values = values[s].replace(d, '')
    if all(eliminate(values, s, d2) for d2 in other_values):
        return values
    else:
        return False


def eliminate(values, s, d):
    if d not in values[s]:
        return values
    values[s] = values[s].replace(d, '')
    if len(values[s]) == 0:
        return False
    elif len(values[s]) == 1:
        d2 = values[s]
        if not all(eliminate(values, s2, d2) for s2 in peers[s]):
            return False

    for u in units[s]:
        dplaces = [s for s in u if d in values[s]]

    if len(dplaces) == 0:
        return False
    elif len(dplaces) == 1:
        if not assign(values, dplaces[0], d):
            return False
    return values


def display(values):
    for r in rows:
        row = []
        for c in cols:
            row.append(values['{}{}'.format(r, c)])
        print(' '.join(row))


def parse_grid(grid):
    values = dict((s, digits) for s in squares)
    for s, d in grid_values(grid).items():
        if d in digits and not assign(values, s, d):
            return False
    return values


def grid_values(grid: list):
    ans = ''
    for row in grid:
        ans += ''.join(row)

    chars = [c for c in ans if c in digits or c in '0.']
    assert len(chars) == 81
    return dict(zip(squares, chars))


def some(seq):
    for e in seq:
        if e:
            return e
    return False


def search(values):
    if values is False:
        return False
    if all(len(values[s]) == 1 for s in squares):
        return values
    n, s = min((len(values[s]), s) for s in squares if len(values[s]) > 1)
    return some(search(assign(values.copy(), s, d)) for d in values[s])


def solution(problem: list):
    display(search(parse_grid(problem)))


def main():
    problem = []
    for _ in range(9):
        problem.append(read_list_str())
    solution(problem)


if __name__ == '__main__':
    main()
