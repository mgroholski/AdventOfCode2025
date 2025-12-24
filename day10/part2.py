"""
Too slow of a solution. I decided to use code I found on Reddit rather than implement something
faster. I've seen similiar problems to this... I'll hopefully get to come back to this after christmas.
"""


def main(inp):
    def minSoln(state, soln, buttons, res):
        if state == soln:
            return res

        valid = True
        for idx in range(len(state)):
            if state[idx] > soln[idx]:
                valid = False
                break

        if not valid:
            return float("inf")

        minRes = float("inf")
        for idx, button in enumerate(buttons):
            newState = state.copy()
            for i in button:
                newState[i] += 1

            minRes = min(minRes, minSoln(newState, soln, buttons[idx:], res + 1))
        return minRes

    res = 0
    for idx, input in enumerate(inp):
        soln = input[-1]
        buttons = input[1]

        res += minSoln([0 for _ in range(len(soln))], soln, buttons, 0)
        print(f"Finished {idx}.")

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

            cleaned_meters = []
            for meter in line_items[-1][1:-1].split(","):
                cleaned_meters.append(int(meter))

            inp.append((list(line_items[0][1:-1]), cleaned_buttons, cleaned_meters))

    main(inp)
