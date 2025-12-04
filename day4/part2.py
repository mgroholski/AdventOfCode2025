def main(grid):
    directions = [(1, 0), (1, 1), (-1, 0), (-1, -1), (0, 1), (0, -1), (-1, 1), (1, -1)]
    m, n = len(grid), len(grid[0])
    res = 0
    roll_cnt = sum([row.count("@") for row in grid])
    l_roll_cnt = 0
    while roll_cnt != l_roll_cnt:
        l_roll_cnt = roll_cnt
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == "@":
                    cnt = 0
                    for di, dj in directions:
                        ni, nj = i + di, j + dj

                        if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == "@":
                            cnt += 1

                    if cnt < 4:
                        grid[i][j] = "."
                        res += 1
                        roll_cnt -= 1

    print(res)


if __name__ == "__main__":
    inp = []
    with open("inp.txt", "r") as file:
        for line in file:
            inp.append(list(line.strip()))

    main(inp)
