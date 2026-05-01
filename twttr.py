#Week 2, problem set 0, Que 3.
#Write a program that takes a string as input and print the output with vowels omitted.
s = input("Input: ")
s1 = ""
for i in s:
    if i not in "aeiouAEIOU":
        s1 += i
print("Output: " + s1)
 