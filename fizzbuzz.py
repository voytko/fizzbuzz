from sys import argv


def main():
    if len(argv) == 2:
        try:
            int_num = int(argv[1])
            print("fizz" * (int_num % 3 == 0) + "buzz" * (int_num % 5 == 0) or int_num)
        except ValueError:
            pass


if __name__ == "__main__":
    main()
