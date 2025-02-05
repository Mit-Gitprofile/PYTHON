import sys

def main():
    # Ensure there are enough arguments
    if len(sys.argv) < 3:
        print("Usage: python sum_lists.py <list1> <list2>")
        sys.exit(1)

    # Extract the lists from command-line arguments
    try:
        list1 = list(map(int, sys.argv[1].split(',')))
        list2 = list(map(int, sys.argv[2].split(',')))
    except ValueError:
        print("Please ensure both lists contain valid integers separated by commas.")
        sys.exit(1)

    # Calculate the sum of all elements
    total_sum = sum(list1) + sum(list2)

    # Print the result
    print(f"Sum of all elements: {total_sum}")

if __name__ == "__main__":
    main()
