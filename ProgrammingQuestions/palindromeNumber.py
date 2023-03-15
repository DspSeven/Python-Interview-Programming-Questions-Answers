number = input()


check = ""
for i in number:
    check = i + check


if(check == number):
    print(number,"is palindrome number")
else:
    print(number,"is not a palindrome number")
