
name = input("What's your name? ")
age = int(input("What's your age? "))
number = int(input("What's your favorite number? "))
century = 2020 + (100-age)
i = 0

while i < number:
        print("Hello {}, you will be 100 in the year {}\n"\
            .format(name, century))
        i += 1