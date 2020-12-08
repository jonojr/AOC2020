

def password_valid(password_details):
    expected_location, letter, password = password_details.split(' ')
    expected_location = [int(locaiton)-1 for locaiton in expected_location.split("-")]
    letter = letter.strip(":")

    return bool(password[expected_location[0]] == letter) ^ bool(password[expected_location[1]] == letter)


with open("input.txt", "r") as input_file:
    passwords = input_file.read().split('\n')

valid_count = 0
for password_details in passwords:
    valid_count += password_valid(password_details)

print valid_count