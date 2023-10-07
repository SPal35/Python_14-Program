# Program to check the validity of password given by user#
user_input = input()
passwords = user_input.split(",")
special_chars = ["$","#","@"]
valid = []

for x in passwords:

    if(len(x) > 12 or len(x) < 6):
        continue

   
    if (x.isupper() or x.islower()): 
        continue
    
    has_number = any(char.isdigit() for char in x)
    if(not has_number):
        continue
    
    has_char = any(char in special_chars for char in x)
    if(not has_char):
        continue

    valid.append(x)
print(valid)