import re

REQUIRED_KEYS = ["byr","iyr","eyr", "hgt","hcl","ecl","pid"]
BYR = range(1920,2003)
IYR = range(2010, 2021)
EYR = range(2020,2031)
HGT_CM = range(150,194)
HGT_IN = range(59,76)
ECL = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def are_keys_valid(passport_dict):
    if len(set(passport_dict.keys()).intersection(set(REQUIRED_KEYS))) == len(REQUIRED_KEYS):
        return True
    return False

def is_valid_year(yr):
    if int(yr) and len(yr) == 4:
        return True

def are_fields_valid(passport_dict):
    if not is_valid_year(passport_dict["byr"]):
        return False
    elif not int(passport_dict["byr"]) in BYR:
        return False
    if not is_valid_year(passport_dict["iyr"]):
        return False
    elif not int(passport_dict["iyr"]) in IYR:
        return False
    if not is_valid_year(passport_dict["eyr"]):
        return False
    elif not int(passport_dict["eyr"]) in EYR:
        return False
    system = passport_dict["hgt"][-2:]
    if not system in ["cm", "in"]:
        return False
    hgt = int(passport_dict["hgt"].replace(system, ""))
    if system == "cm":
        if not int(hgt) in HGT_CM:
            return False
    else:
        if not int(hgt) in HGT_IN:
            return False
    if not passport_dict["ecl"] in ECL:
        return False

    if passport_dict["hcl"][0] != "#":
        return False
    if len(passport_dict["hcl"]) != 7:
        return False
    pattern = re.compile("[a-f0-9]+")
    if pattern.fullmatch(passport_dict["hcl"][1:]) is None:
        return False
    if len(passport_dict["pid"]) != 9:
        return False
    if not passport_dict["pid"].isalnum():
        return False
    return True

def create_records(input_string):
    records = []
    record = {}
    for l in input_string:
        if l != "\n":
            line = l.strip("\n")
            field_val = line.split(" ")
            for fv in field_val:
                k,v = fv.split(":")
                record[k] = v
        else:
            records.append(record)
            record = {}
    records.append(record)
    return records

if __name__ == "__main__":
    with open("aoc-input-4.txt","r") as f:
        input_string = f.readlines()
    records = create_records(input_string)
    count_1 = 0
    count_2 = 0
    for record in records:
        if are_keys_valid(record):
            count_1 += 1
            if are_fields_valid(record):
                count_2 += 1
    print("part1: {}".format(count_1))
    print("part2: {}".format(count_2))
