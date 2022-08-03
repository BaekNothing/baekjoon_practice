charMap = {
    '.' : '.',
    'O' : 'O',
    '-' : '|',
    '|' : '-',
    '/' : '\\',
    '\\' : '/',
    '^' : '<',
    '<' : 'v',
    'v' : '>',
    '>' : '^'
}

height, width = map(int, input().split())

oldLine = []
for i in range(height):
    inputCharList = list(input())
    oldLine.append(inputCharList)

rotatedLine = [['' for i in range(height)] for j in range(width)]
for i in range(height):
    for j in range(width):
        rotatedLine[j][i] = charMap[oldLine[i][j]]
rotatedLine.reverse()
print ('\n'.join(''.join(row) for row in rotatedLine))