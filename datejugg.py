def palindrome_test_function(self):
    def check_palidrome(thestring):
      if thestring == thestring[::-1]:
        return True
      else:
        return False
    return check_palidrome(thestring)


test_function = palindrome_test_function
print test_function('aba')
