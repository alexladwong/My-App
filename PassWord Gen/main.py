import random

characters = "abcdefghijklmnopgrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" \
             "©!@#$%^&*()_`~¸˘˜˛˛≥ˇÆ«‘“Øʼ¨¥Þ®´´"
while True:
    pass_length = int(input("Please enter the Length of your strong password here: "))
    pass_count = int(input("How many passwords do you want me to generated? "))

    for i in range(0, pass_count):
        password = ""
        for j in range(0, pass_length):
            pass_char = random.choice(characters)
            password = password + pass_char

        print("Your Generated password is: ", password)

    repeat = input("Do you want me to generate more passwords for you? ")
    if repeat == "no" or repeat == "No":
        break

print("Thanks you! ")
