# This function adds two numbers
def add(x, y):
    print(f"{x + y}")

# This function subtracts two numbers
def subtract(x, y):
    print(f"{x - y}")

# This function multiplies two numbers
def multiply(x, y):
    print(f"{x * y}")


# This function divides two numbers
def divide(x, y):
    print(f"{x / y}")


def new_df(*args):
    sum_all = 0 
    for i in args:
        sum_all += i

    print(sum_all)



mal = new_df(1,2,3)

print(mal)

# print("cal modual for all data")

# print(__name__)
    

# if __name__ == "__main__":
#     print("cal modual for all data")
    

