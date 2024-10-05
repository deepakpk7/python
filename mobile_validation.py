import re
# a='7034622523'
# if len(a)==10 and re.search('[6-9].{9}',a) and a.isdigit():
#     print('valid')
# else:
#     print('not valid')
    
a=input("Enter a password")
if len(a)>=8 and re.search('^[A-z0-9].*[!@#$%&0-9]',a) and not(a.isdigit()):
    print("Password changed")
else:
    print("Incorrect password")