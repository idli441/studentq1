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


#2nd way

import math

def calculate_statistics():
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    
    # Calculate mean
    mean = sum(nums) / len(nums)
    
    # Calculate variance
    variance = sum((x - mean) ** 2 for x in nums) / len(nums)
    
    # Calculate standard deviation
    std_dev = math.sqrt(variance)
    
    print(f"Mean: {mean}\nVariance: {variance}\nStandard Deviation: {std_dev}")

def main():
    print("=== Mean, Variance, Standard Deviation ===")
    calculate_statistics()

if __name__ == "__main__":
    main()

