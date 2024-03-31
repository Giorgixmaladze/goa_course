
#შევქმენით ცვლადი სადაც შეტანილია სია რომელშიც წერია სტრინგის სახით თამაშების სახელები

# games = ["Grand theft auto","counter strike","minecraft","fortnite"]


#ჩავანაცვლეთ თამაშის სახელები სხვა თამაშის სახელებით
# games[0] ="codewars"
# games[1] = "kahoot"
# games[2] = "sololearn"
# games[3] = "codemonkey"

#გამოვიტანეთ ეს ყველაფერი print ფუნქციის საშუალებით
# print(games)







#მომხმარებელს შემოვატანინეთ 5 მნიშვნელობა
number1 = int(input("Enter the first number:"))
number2 = int(input("Enter the second number:"))
number3 = int(input("Enter the third number:"))
number4 = int(input("Enter the fourth number:"))
number5 = int(input("Enter the fifth number:"))


#შევქმენით სია სადაც შენახულია მომხმარებლის მიერ შემოტანილი მონაცემები
numbers = [number1,number2,number3,number4,number5]


print(numbers)



#თუ შემოტანილი რიცხვები არის ლუწი ვეუბნებით მომხმარებელს რომ ეს რიცხვი ლუწია ხოლო თუ კენტია ვამბობთ რომ რიცხვი არის
if numbers[0] % 2 == 0:
    print("First number is even")
else:
    print("the first number is odd")

if numbers[1] % 2 == 0:
    print("Second number is even")
else:
    print("the Second number is odd")


if numbers[2] % 2 == 0:
    print("Third number is even")
else:
    print("The third number is odd")

if numbers[3] % 2 == 0:
    print("Fourth number is even")
else:
    print("The Fourth number is odd")
if numbers[4] % 2 == 0:
    print("Fifth number is even")
else:
    print("The fifth number is odd")











