# import graph
# import antworld

antGrid = [[1,1,1],[1,1,1],[1,1,1]]
nodeGrid = None


def printGrid():
    for row in antGrid:
        row_string = ''
        for node in row:
            row_string += 'x - '
        print(row_string[:-3])
        row_string = ''
        for node in row:
            row_string += '|   '
        print(row_string[:-3])