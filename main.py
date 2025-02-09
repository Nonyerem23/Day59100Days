
def palindrome(word):
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return palindrome(word[1:-1])

print()
print("🌟Palindrome Checker🌟")
print()
word = input("Input a word > ")
print()
if palindrome(word):
    print(f"{word} is a palindrome. Yay!")
else:
    print(f"{word} is not a palindrome. Sorry!")

print()
# palindrome test cases
print(palindrome("racecar"))

print(palindrome("hello"))