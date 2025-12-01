with open("inp.txt", "r") as file:
    location = 50
    res = 0

    for line in file:
        dir, cnt = 1 if line[0] == "R" else -1, int(line[1:])

        location = (location + dir * cnt) % 100
        if not location:
            res += 1

    print("Zero Count: ", res)
