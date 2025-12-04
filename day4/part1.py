def main(grid):
    directions = [(1, 0), (1, 1), (-1, 0), (-1, -1), (0, 1), (0, -1), (-1, 1), (1, -1)]
    m, n = len(grid), len(grid[0])
    res = 0

    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == "@":
                cnt = 0
                for di, dj in directions:
                    ni, nj = i + di, j + dj

                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == "@":
                        cnt += 1

                if cnt < 4:
                    res += 1

    print(res)


if __name__ == "__main__":
    inp = []
    with open("inp.txt", "r") as file:
        for line in file:
            inp.append(list(line.strip()))

    main(inp)
