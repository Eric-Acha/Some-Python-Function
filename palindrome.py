# Find out if a word is thesame when it is reversed

word = input("enter a word: ")
is_palindrome = True if word == word[::-1] else "No"
print(is_palindrome)
