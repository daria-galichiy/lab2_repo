def reverse_string(input_string):
    index = len(input_string) - 1
    reversed_string = ""

    for _ in input_string:
        reversed_string += input_string[index]
        index -= 1
    # return(input_string[::-1])
    return reversed_string


def main():
    str = "hello, world"
    print(reverse_string(str))


main()