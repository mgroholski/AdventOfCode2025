def main(inp):
    def minSoln(state, soln, buttons, res):
        if state == soln:
            return res

        minRes = float("inf")
        for idx, button in enumerate(buttons):
            newState = state.copy()
            for i in button:
                newState[i] = "." if state[i] == "#" else "#"

            minRes = min(minRes, minSoln(newState, soln, buttons[idx + 1 :], res + 1))
        return minRes

    res = 0
    for input in inp:
        soln = input[0]
        buttons = input[1]

        res += minSoln(["." for _ in range(len(soln))], soln, buttons, 0)

    print(res)


if __name__ == "__main__":
    inp = []

    with open("inp.txt", "r") as file:
        for line in file:
            line_items = line.strip().split(" ")

            buttons = line_items[1:-1]
            cleaned_buttons = []
            for button in buttons:
                cleaned_buttons.append([int(b) for b in button[1:-1].split(",")])

            inp.append((list(line_items[0][1:-1]), cleaned_buttons, line_items[-1]))

    main(inp)
