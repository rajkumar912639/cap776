# A function to check if a string is a palindrome
def is_palindrome(s):
  # Reverse the string using slice notation
  reversed_s = s[::-1]
  # Compare the original and reversed strings
  if s == reversed_s:
    # The string is a palindrome
    return True
  else:
    # The string is not a palindrome
    return False

# Test the function with some examples
print(is_palindrome("racecar")) # True
print(is_palindrome("hello")) # False
print(is_palindrome("madam")) # True

