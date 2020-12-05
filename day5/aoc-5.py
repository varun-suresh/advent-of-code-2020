def convert_to_int(input_str, upper):
    n = 0
    for idx, char in enumerate(input_str):
        if char == upper:
            n += pow(2,len(input_str) - idx-1)
    return n

if __name__ == "__main__":
    with open("aoc-input-5.txt", "r") as f:
        lines = f.readlines()
        seat_ids = []
    for l in lines:
        line = l.strip("\n")
        row_number = convert_to_int(line[0:7], upper="B")
        column_no = convert_to_int(line[7:], upper="R")
        seat_ids.append(row_number*8 + column_no)
    print("part_1")
    print(max(seat_ids))
    seat_ids = set(seat_ids)
    print("part_2")
    for i in range(min(seat_ids), max(seat_ids)+1):
        if not i in seat_ids and i-1 in seat_ids and i+1 in seat_ids:
            print(i)
