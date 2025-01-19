# Checking palindrom

enter_word = input("Enter the word")

if enter_word == enter_word[::-1]:
    print("This is palindrom number")
else:
    print("This is not palindrom")
