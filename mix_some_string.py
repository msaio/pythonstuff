from sys import argv

file_name, str_1, str_2 = argv

# First of all, i recommend 2 string with the same length, not compulsorily
# Explain how it works
print("This is what zip() return:")
x = zip(str_1,str_2)
print (x)

print("\nGet every item in zip_list above and match them in pairs, also return a list: ")
x = ["".join(x) for x in zip(str_1,str_2)]
print(x)

print("\nNow, unite into a string: ")
x = "".join(["".join(x) for x in zip(str_1,str_2)])
print x

print("------------")

mixed_str = "".join(["".join(x) for x in zip(str_1,str_2)])
print("Result:")
print(mixed_str)

print("\n[::2]:")
print(mixed_str[::2])

print("\n[1::2]:")
print(mixed_str[1::2])