sentence = input("Enter the sentence: ")
string = sentence.lower()
count = 0
vowels = "aeiou"
for char in string:
    if char in vowels:
        count += 1
print("Number of vowels in given sentence is: ", count)
#مش شغالة هنا بش المفروض تعمل ان اي حرف small  يشملها
