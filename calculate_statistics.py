import numpy as np

def calculate_statistics():
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    mean, var, std = np.mean(nums), np.var(nums), np.std(nums)
    print(f"Mean: {mean}\nVariance: {var}\nStandard Deviation: {std}")

def main():
    print("=== Mean, Variance, Standard Deviation ===")
    calculate_statistics()

if __name__ == "__main__":
    main()
