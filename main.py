from letter_combinations import letter_combinations

def main():

    digits = "23"
    result1 = sorted(letter_combinations(digits))
    print("Example 1:")
    print(f"digits = \"{digits}\"")
    print(f"Output: {result1}")
    
    digits = ""
    result2 = sorted(letter_combinations(digits))
    
    print("Example 2:")
    print(f"digits = \"{digits}\"")
    print(f"Output: {result2}")
    
    digits3 = "234"
    result3 = sorted(letter_combinations(digits3))
    
    print("Example 3:")
    print(f"digits = \"{digits3}\"")
    print(f"Output: {result3}")

if __name__ == "__main__":
    main()
