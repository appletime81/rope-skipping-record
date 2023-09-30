from pprint import pprint


def cal(filename):
    with open(filename, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    totalSum = []
    tempTotal = 0
    for i, line in enumerate(lines):
        if line.isdigit():
            tempTotal += int(line)
            if i + 1 == len(lines) or not lines[i + 1].isdigit():
                print(f"This time: {tempTotal}")
                totalSum.append(tempTotal)
                tempTotal = 0
                print("-" * 100)

    print(f"Total: {sum(totalSum)}")


if __name__ == "__main__":
    filename = "records29.txt"
    cal(filename)
