def letter_by_letter(string):
    import time
    for word in string:
        print(word, end='')
        time.sleep(.10)
    print()


def loading():
    import time
    for char in "Loading...":
        print(char, end='')
        time.sleep(.10)
    print(chr(9203))
