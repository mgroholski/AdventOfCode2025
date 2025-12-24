"""
We're looking to count the different paths from 'you' to 'out'. We'll structure the input as a directed graph,
we're not guranteed an acyclic graph, so we'll want to use a visit set.
"""


def main(nodes):
    res = 0

    # seenSet = set()
    stack = ["you"]
    while stack:
        u = stack.pop()

        if u == "out":
            res += 1

        if u in nodes:
            for v in nodes[u]:
                stack.append(v)

    print(res)


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
