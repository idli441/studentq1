def pair_sum():
    nums = list(map(int, input("Enter numbers: ").split()))
    target = int(input("Enter target sum: "))
    lookup = {}
    for i, num in enumerate(nums):
        if target - num in lookup:
            print(f"Indices: {lookup[target - num]}, {i}")
            return
        lookup[num] = i
    print("No such pair found.")

def main():
    print("=== Pair Sum to Target ===")
    pair_sum()

if __name__ == "__main__":
    main()
