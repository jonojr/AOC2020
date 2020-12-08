from re import match


def process_passport_batch(passport_batch):
    results = []
    for passport_string in passport_batch:
        processed_string = passport_string.replace(' ', '","').replace('\n', '","').replace(':', '":"')
        processed_string = f'{{"{processed_string}"}}'

        results.append(eval(processed_string))

    return results


def validate_byr(byr):
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    return 1920 <= int(byr) <= 2002


def validate_iyr(iyr):
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    return 2010 <= int(iyr) <= 2022


def validate_eyr(eyr):
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    return 2020 <= int(eyr) <= 2030


def validate_hgt(hgt):
    # hgt (Height) - a number followed by either cm or in:
    #     If cm, the number must be at least 150 and at most 193.
    #     If in, the number must be at least 59 and at most 76.
    measurement_type = hgt[-2:]
    if measurement_type not in ["cm", "in"]:
        return False

    measurement_value = int(hgt[:-2])
    if measurement_type == "cm":
        return 150 <= measurement_value <= 193
    if measurement_type == "in":
        return 59 <= measurement_value <= 76

    return False


def validate_hcl(hcl):
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    return match("^#([a-f]|[0-9]){6}$", hcl)


def validate_ecl(ecl):
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    return ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def validate_pid(pid):
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    return match("^[0-9]{9}$", pid)


def passport_valid(passport):
    required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    # cid (Country ID) - ignored, missing or not.

    missing_fields = required_fields - passport.keys()

    if bool(missing_fields):
        return False

    return all(
        [
            validate_byr(passport["byr"]),
            validate_iyr(passport["iyr"]),
            validate_eyr(passport["eyr"]),
            validate_hgt(passport["hgt"]),
            validate_hcl(passport["hcl"]),
            validate_ecl(passport["ecl"]),
            validate_pid(passport["pid"]),
        ]
    )


if __name__ == "__main__":
    with open("input.txt", 'r') as input_file:
        passport_batch = input_file.read().split("\n\n")

    valid_count = 0
    for passport in process_passport_batch(passport_batch):
        valid_count += passport_valid(passport)

    print(valid_count)



