def count_trees(input_string, horizontal_ptr_increment, vertical_step):
    horizontal_ptr = 0
    count = 0
    for i, l in enumerate(input_string):
        if i % vertical_step == 0:
            line = l.strip("\n")
            if line[horizontal_ptr % len(line)] == "#":
                count += 1
            horizontal_ptr += horizontal_ptr_increment
    return count

if __name__ == "__main__":
    with open("aoc-input-3.txt", "r") as f:
        input_string = f.readlines()
    print("Part 1:")
    print(count_trees(input_string,3,1))
    print("Part 2:")
    h_increments = [1,3,5,7,1]
    v_increments = [1,1,1,1,2]
    prod = 1
    for i,j in zip(h_increments,v_increments):
        # print(count_trees(input_string, i, j))
        prod *= count_trees(input_string, i, j)
    print(prod)
