import collections

def top_words():
    filename = input("Enter file name: ")
    try:
        word_count = collections.Counter(open(filename).read().split())
        for word, count in word_count.most_common(10):
            print(f"{word}: {count}")
    except FileNotFoundError:
        print("File not found!")

def main():
    print("=== Top 10 Words in File ===")
    top_words()

if __name__ == "__main__":
    main()
