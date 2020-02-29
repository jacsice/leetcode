
def fib(n):
    f = [0, 1]
    for i in range(n):
        f.append(f[i] + f[i+1])
    return f[n]


def maze():
    maze_arr = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [1, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 1, 0],
        [0, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]
    path_dict = {}
    for i in range(8):
        path_dict['7%s' % i] = 1
        path_dict['%s7' % i] = 1
    for x in range(6, -1, -1):
        for y in range(6, -1, -1):
            x_down = path_dict['%s%s' % (x+1, y)] if maze_arr[x+1][y] == 0 else 0
            y_right = path_dict['%s%s' % (x, y+1)] if maze_arr[x][y+1] == 0 else 0
            path_dict['%s%s' % (x, y)] = x_down + y_right

    print(path_dict['00'])





if __name__ == '__main__':
    print(maze())