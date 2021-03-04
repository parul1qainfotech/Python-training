#Write a Python class which has two methods get_String and print_String. get_String accept a string from the user and print_String print the string in upper case.

class Strings:
    def get_String(self):
        self.inp=str(input())
    def print_String(self):
        print(self.inp.upper())
        
s1=Strings()
s1.get_String()
s1.print_String()