def check_palindrome(word):
  word = word.lower()
  return word[::-1] == word
print(check_palindrome('Mom'))