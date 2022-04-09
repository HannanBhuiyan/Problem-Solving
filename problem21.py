# problem: Test whether a passed letter is a vowel or not

# WAY ONE
char1 = input()
char = char1.lower()
if char == "a" or char == "e" or char == "i" or char == "0" or char == "u":
    print("Vowel")
else:
    print("Consonant")


# WAY TWO
def is_vowel(char):
    all_vawel_leters = "aeiou"
    return char.lower() in all_vawel_leters


print(is_vowel("F"))
