
# let make a function from our get in program (see esceptions.py)


def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x should be an integer")
        else:
            break
    return x

main()