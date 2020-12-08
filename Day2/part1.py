

def password_valid(password_details):
    expected_count, letter, password = password_details.split(' ')
    expected_count = [int(count) for count in expected_count.split("-")]
    letter = letter.strip(":")

    letter_count = password.count(letter)
    return expected_count[0] <= letter_count <= expected_count[1]


with open("input.txt", "r") as input_file:
    passwords = input_file.read().split('\n')

valid_count = 0
for password_details in passwords:
    valid_count += password_valid(password_details)

print valid_count