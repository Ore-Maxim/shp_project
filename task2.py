def count_digits(s):
    return sum(1 for char in s if char.isdigit())

if __name__ == "__main__":
    text = input()
    print(count_digits(text))
