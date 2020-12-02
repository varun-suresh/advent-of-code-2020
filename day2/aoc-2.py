
def policy_1(input_string):
    lower_limit = int(input_string.split("-")[0])
    upper_limit = ""
    for c in input_string.split("-")[1]:
        if c != " ":
            upper_limit += c
        else:
            break
    upper_limit = int(upper_limit)
    pwd_char = input_string.split(":")[0][-1]
    pwd = input_string.split(":")[1][1:]
    print(lower_limit, upper_limit, pwd_char, pwd)
    if pwd.count(pwd_char) >= lower_limit and pwd.count(pwd_char) <= upper_limit:
        return True
    return False

def policy_2(input_string):
    first_pos = int(input_string.split("-")[0])
    second_pos = ""
    for c in input_string.split("-")[1]:
        if c != " ":
            second_pos += c
        else:
            break
    second_pos = int(second_pos)
    pwd_char = input_string.split(":")[0][-1]
    pwd = input_string.split(":")[1][1:]
    if (pwd[first_pos - 1] == pwd_char) ^ (pwd[second_pos-1] == pwd_char):
        return True
    return False

if __name__ == "__main__":
    # input_string = "2-9 c: ccccccccc"
    # print(policy_2(input_string))
    with open("aoc-input-2.txt", "r") as f:
        lines = f.readlines()
    count = 0
    for line in lines:
        # print(line.strip("\n"))
        if policy_2(line.strip("\n")):
            count += 1

    print(count)
