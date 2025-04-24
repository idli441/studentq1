def sort_file():
    filename = input("Enter file name: ")
    try:
        with open(filename) as f:
            lines = sorted(f.readlines())
        with open("sorted_" + filename, "w") as f:
            f.writelines(lines)
        print(f"Sorted contents saved to sorted_{filename}")
    except FileNotFoundError:
        print("File not found!")

def main():
    print("=== Sort File Content ===")
    sort_file()

if __name__ == "__main__":
    main()
