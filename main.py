 # -------------------------- Tech-Amb Track -------------------------
 # Ahmed Abdel Hameed Abdel Qader : ahmadhamid92@outlook.com

#   ============================================================

#   Program 01 : Write a program that counts up the number of vowels [a, e, i, o, u] contained in the string
#region 01

# vowels = 'aeiou'
#
# # take an input from the user
#
# input_str = input("Enter a string: ")
#
# # make it suitable for caseless comparisions
#
# input_str = input_str.casefold()
#
# count = {}.fromkeys(vowels,0)
#
# # count the vowels
#
# for char in input_str:
#
#    if char in count:
#
#        count[char] += 1
#
# print(count)

#endregion

# ===================================================================================================
#  Program 02:  Write a function that accepts two arguments (length, start) to generate an array of a specific length filled with integer numbers increased by one from start.
 #region 02

 # function definition
# def generate_array(start,length):
#    for i in range(start,length+1):
#       print(i)
#
#  # function call
# start=int(input("Enter the start of loop :"))
# length=int(input("Enter the Length of loop :"))

# generate_array(start,length)


 #endregion

 # ===============================================================================================
 # Program 03 : Fill an array of 5 elements from the user, Sort it in descending and ascending orders then display the output from array import array

#region 03
# def get_array(array=[]):
#      array.sort()
#      print("Ascending ",array)
#      array.reverse()
#      print("Descinding ",array)
#
# print("Input six integers:")
# nums = list(map(int, input().split()))
# # lst1 = [int(item) for item in input("Enter the list items : ").split()
# get_array(nums)

#endregion

# ===================================================================================
# Program 04 :  write a function that takes a number as an argument and if the number divisible by 3 return "Fizz" and if it is divisible by 5 return "buzz" and if is is
# divisible by both return "FizzBuzz"

#region 04

# def fizz_buzz(number):
#     if number % 3 ==0 and number % 5 !=0 :
#         print("Fizz")
#     elif number % 5 ==0 and number % 3 !=0 :
#         print("Buzz")
#     elif number % 3 ==0 and number % 5 ==0 :
#         print("FizzBuzz")
#     else:
#         print(0)
#
# # function call
# number = int(input("Enter the number"))
# fizz_buzz(number)


#endregion

# ======================================================================================
# Program 05 :  Write a function which has an input of a string from user then it will return the same string reversed

 #region 05

# def string_reverse(word):
#     print(word[::-1]) # slicing
#
#  # function call
# word=input("Enter the paragraph:  ")
# string_reverse(word)
 #endregion

 # =====================================================================================
 # program 06: Ask the user to enter the radius of a circle in order to alert its calculated area and circumference

 #region 06
# def circle_area_circum(radius,PI = 3.14):
#     print("Area",PI * radius * radius )
#     print("Circum", 2 * PI * radius)
#
# r = float(input("Enter the radius of a circle:"))
# circle_area_circum(r)

 #endregion

# =====================================================================================
 # program 07:Ask the user for his name then confirm that he has entered his name  (not an empty string/integers). then proceed to ask him for his email and
 # print all this data   - (Bonus) check if it is a valid email or not

 #region 07

# import re
# regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
#
#
# def print_name_email(name,email):
#     if len(name) and  re.search(regex,email):
#         print(f"Name is : {name} , Email is : {email}")
#     else:
#         print("Please Enter valid fields !")
#
# name=input("Enter the Name : ")
# email=input("Enter the Email : ")
# print_name_email(name,email)

 #endregion

# =====================================================================================
 # program 08: Write a program that prints the number of times the string 'iti' occurs in

#region 08

# def count_iti(paragraph,searchSegment):
#     count = paragraph.count(searchSegment)
#     print(f"The substring ' {searchSegment} ' occurs {count} times")
#
# paragraph=input("Enter the Paragraph ")
# searchSegment=input("Enter the word to Search ")
# count_iti(paragraph,searchSegment)
#endregion

# =====================================================================================
 # program 09: Write a function that takes a string and prints the longest alphabetical ordered substring occured.
# For example, if the string is 'abdulrahman' then the output is: Longest substring in alphabetical order is: abdu

#region 09


# def longest_alphabetical(paragraph):
#     prevChar = ""
#     curr_longest = ""
#     longest = ""
#     for char in paragraph:
#         if (prevChar.lower() <= char.lower()):
#             curr_longest += char
#             if len(curr_longest) > len(longest):
#                 longest = curr_longest
#         else:
#             curr_longest = char
#         prevChar = char
#     print(longest)
#
# paragraph=input("Enter the parargaph : ")
# longest_alphabetical(paragraph)

#endregion
