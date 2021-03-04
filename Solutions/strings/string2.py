#Split a given string on hyphens into several substrings and display each substring:

str1 = "Emma-is-a-data-scientist"
substring=str1.split("-")
for i in substring:
    print(i)