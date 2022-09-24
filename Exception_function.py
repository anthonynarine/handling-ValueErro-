
# let make a function from our get in program (see esceptions.py)

def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
        except ValueError:
            print("x should be an integer")
        else:
            return x  #return can be used to both break and return a value

main()