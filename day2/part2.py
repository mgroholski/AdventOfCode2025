"""
The problem changes to determining if it is made of some sequence of digits repeated at least twice.
We'll want to iterate over over number in each range. However, for each number how do we determine if it's a repeating number?

These problems have typically been solved using dynamic programming. Given some part of the substring s, is s a repeating sequence?
We iterate over previous s's.
1. If there is no previous, s we need to determine if there's one partition point (the middle of the substring).
2. If there is a previous s, we need to determine if the newly added characters since
that last true match the sequence.


"""


def validNumber(i):
    str_i = str(i)
    dp = [[] for _ in range(len(str_i))]

    for j in range(1, len(str_i)):
        val = []
        for k in range(j):
            if len(dp[k]):
                for s in dp[k]:
                    if s == str_i[k + 1 : j + 1]:
                        val.append(s)

        if str_i[: (j + 1) // 2] == str_i[(j + 1) // 2 : j + 1]:
            val.append(str_i[: (j + 1) // 2])
        dp[j] = val

    return len(dp[-1]) > 0


def main(ranges):
    res = 0

    # print(validNumber("12121"))

    for s, e in ranges:
        for i in range(s, e + 1):
            if validNumber(i):
                res += i

    print(res)


if __name__ == "__main__":
    ranges = []
    with open("inp.txt", "r") as text:
        inp = ""
        for line in text:
            inp += line

        ranges_str = inp.split(",")
        for r in ranges_str:
            a, b = r.split("-")
            ranges.append([int(a), int(b)])

    main(ranges)
