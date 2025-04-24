import itertools

def unique_subsets():
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    subsets = [list(sub) for i in range(len(nums)+1) for sub in itertools.combinations(nums, i)]
    print("Subsets:", subsets)

def main():
    print("=== Unique Subsets ===")
    unique_subsets()

if __name__ == "__main__":
    main()
