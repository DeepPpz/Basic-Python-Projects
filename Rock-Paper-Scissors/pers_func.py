def letter_by_letter(string):
    import time
    for char in string:
        print(char, end='')
        time.sleep(.12)
    print()


def loading():
    import time
    for char in "Loading...":
        print(char, end='')
        time.sleep(.10)
    print()


