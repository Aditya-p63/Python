
# LIST
# numbers = [1,2,3,4,5,6,7,8,9]
# print(numbers[0])
# fruits = ["apple", "banana", "cherry"]
# mixed = [1,"apple", True, "cherry"]
# numbers.append(10)
# print(numbers)
# print(mixed)

# TUPPLE
# colors = ["red","green","blue","yellow","purple"]
# print(colors)

# Dictionary
# information = {"Name":"Aditya","Age":29,"Gender":"Male"}
# print(information)
# information["Address"]="powai"
# print(information)
# information["Age"]=30
# print(information)
# if "grade" in information:
#     del information["grade"]
# print(information)
#
# freq count

stri = input()
words = stri.split()
word_count = {}
for i in words:
    i = i.lower()
    if i in word_count:
        word_count[i] += 1
    else:
        word_count[i] = 1

print(word_count)