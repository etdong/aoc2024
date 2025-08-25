import io


def part1(left, right):
    left.sort()
    right.sort()

    total = 0
    for i in range(len(left)):
        total += abs(left[i] - right[i])
    return total

def part2(left, right):
    total = 0
    for i in left:
        total += right.count(i) * i
    return total


if __name__ == "__main__":
    input_data = io.FileIO("day1/input.txt", "r").read().decode("utf-8").strip()
    numbers = list(input_data.splitlines())
    left, right = [], []
    for i in numbers:
        nums = i.split()
        left.append(int(nums[0]))
        right.append(int(nums[1]))

    print(part1(left, right))
    print(part2(left, right))