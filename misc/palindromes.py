word=(input("enter a word: "))
def palindromes(word):
     if word[::-1]==word:
          print("your word you entered is palindrome")
     else:
          print("sorry your word is not a palindrome")
palindromes(word)               