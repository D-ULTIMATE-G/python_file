# this program is to count the number of voweis in a sentenced

sentence = input("enter the sentence")
str = sentence.lower()
print("string")
count = 0
list1 = ("a", "e", "i", "o", "u")
for char in str:
    if char in list1:
        count =count+1
print("vowels letter in given sentence is:",count)

