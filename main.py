# AutoTesting-AT/main.py

def count_vowels(s: str) -> int:
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

if __name__ == "__main__":
    example_string = "Hello World!"
    print(f"The number of vowels in '{example_string}' is {count_vowels(example_string)}")
