TARGET = 2020

def part_1(numbers):
    # print(numbers)
    # numbers = [1721,979,366,299,675,1456]
    complements = set()
    for number in numbers:
        # print(number)
        # print(complements)
        if TARGET-number in complements:
            print(number, TARGET-number)
            print(number*(TARGET-number))
            break
        else:
            complements.add(number)
    # print(complements)


#Part 2:
def part_2(numbers):
    found_flag = 0
    for number in numbers:
        new_target = TARGET-number
        complements = set()
        if found_flag == 0:
            for number_2 in numbers:
                if new_target-number_2 in complements:
                    print(number, number_2, new_target-number_2)
                    # print(number*(TARGET-number))
                    print(number*number_2*(new_target-number_2))
                    found_flag = 1
                    break
                else:
                    complements.add(number_2)
        else:
            break

if __name__ == "__main__":
    with open("aoc-input-1.txt") as f:
        lines = f.readlines()
    numbers = [int(line.strip("\n")) for line in lines]
    print("Part 1")
    part_1(numbers)
    print("Part 2")
    part_2(numbers)
