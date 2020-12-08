
def process_passport_batch(passport_batch):
    results = []
    for passport_string in passport_batch:
        processed_string = passport_string.replace(' ', '","').replace('\n', '","').replace(':', '":"')
        processed_string = f'{{"{processed_string}"}}'

        results.append(eval(processed_string))

    return results


def passport_valid(passport):
    required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}  # Missing cid because we are told to ignore it.

    missing_fields = required_fields - passport.keys()

    return not bool(missing_fields)


# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)
if __name__ == "__main__":
    with open("input.txt", 'r') as input_file:
        passport_batch = input_file.read().split("\n\n")

    valid_count = 0
    for passport in process_passport_batch(passport_batch):
        print(passport, passport_valid(passport))
        valid_count += passport_valid(passport)

    print(valid_count)