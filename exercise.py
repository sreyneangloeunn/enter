# ex1
# text = input ("enter word")
# for cha in text:
#     print(cha)

# ex2
# text = input("enter your word : ")
# for i in range(len(text)):
#     print(i)

# ex3
text = input("enter your word: ")
result = "No"
index = 0 
while index in range (len(text)):
    if text[index].isupper():
        result = ("Yes")
    index += 1
print(result)
    
# 4
# text = "3 4 5 6"
# total = 0
# for i in range(len(text)):
#     if text[i] != " ":
#         print(text[i])
#         total += int(text[i])
# print(total)

# # 5
# # Q1
# text = "454639"
# even_num = 0
# odd_num = 0
# for i in range (len(text)):
#     if int(text[i]) % 2 == 0:
#         even_num += 1
#     else:
#         odd_num += 1
# print("enter even number=",even_num)
# print("enter odd number=", odd_num)

# # Q2
# text = "454639"
# sum = 0
# for char in text:
#     if char == text:
#         print(char)
#     sum += int(char)
# print(sum)

# Q3
# text = "454639"
# sum = 0
# for char in text:
#     if int(char) % 2 == 0:
#         sum += int(char)
# print(sum)

# Q4
# text = "454639"
# result = ""
# last_index = len(text)-1
# for i in range (len(text)):
#     result += text[last_index-i]
# print(result)

#6
# number = input("enter your number : ")
# if int(number) % 2 == 1:
#     print("odd")
# else:
#     print("even")

#7
# isFound = False
# while not isFound:
#     num = input("enter your number")
#     if int(num) >= (10) and int(num) <=(20):
#         print("continue")
#     else:
#         print("false")
#         isFound = True

#8
# Q1 - How many number 8 in string
# text = "9394884039"
# result = 0
# for i in range (len(text)):
#         if (text[i]) == "8":
#             result += 1
# print(result)

# Q2 - What is first index of letter 8
# text = "9394884039"
# isFound = False
# index = 0
# while not isFound:
#     if text[index] == "8":
#         isFound = True
#         print(index)
#     index += 1

#9
# Q1
# text = "3 4 5 6"
# result = ""
# for i in range (len(text)):
#     if text[i] != " ":
#         result += text[i]
# print(result)

# Q2
# text = "3 4 5 6"
# result = ""
# for i in range (len(text)):
#     if text[i] != " ":
#         result += str(int(text[i])*2) + " "
# print(result)


# Ex10 - Number
# Enter 5 numbers and find maximum and minimum value
# Example:
# 1
# 5
# 6
# 7
# 0
# output : Max = 7, Min = 0

# max = 0
# min = 0
# for i in range (5):
#     num = input("neter number")
#     if i == 0 :
#         max = num
#         min = num
#     else:
#         if num > max:
#             max = num
#         if num < min:
#             min = num
# print("max", max)
# print("min", min)
