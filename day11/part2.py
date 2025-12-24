"""
We'll need to determine how to get around the engineering restrictions of this. Right now we're getting recursion depth errors.
https://adventofcode.com/2025/day/11
"""

from functools import cache


def main(nodes):
    nodes = nodes

    @cache
    def dfs(u, seenDac, seenFft):
        if u == "out":
            if seenDac and seenFft:
                return 1
            else:
                return 0

        res = 0
        nonlocal nodes
        for v in nodes[u]:
            res += dfs(
                v, True if u == "dac" else seenDac, True if u == "fft" else seenFft
            )

        return res

    print(dfs("svr", False, False))


if __name__ == "__main__":
    nodes = {}
    with open("inp.txt", "r") as file:
        for line in file:
            line = line.strip()
            u, vList = line.split(":")
            vList = vList.strip()

            nodes[u] = []
            curStr = ""
            for l in vList:
                if l == " ":
                    nodes[u].append(curStr)
                    curStr = ""
                else:
                    curStr += l
            nodes[u].append(curStr)

    main(nodes)
