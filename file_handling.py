# f=open('python/dpk.txt','x')
# f=open('python/dpk.txt','r')
# f.write('Welcome to VS Code')
# print(f.read())

# a=f.read(5)

# f.seek(3)
# b=f.read()
# print(f.tell())
# print(a)
# print("_"*20)
# print(b)

# f=open('python/dpk.txt','r')
# a=f.readline(5)
# print(a)
# b=f.readline()
# print(b)
# f.seek(0)
# c=f.readlines()
# print(c)

# f=open('python/dpk.txt','r')
# l=f.readlines()
# f.seek(0)
# for i in range(len(l)):
#     a=f.readline().strip()
#     print(a)
    
# f=open('python/dpk.txt','r')
# l=f.readlines()
# f.seek(0)
# for i in range(len(l)):
#     a=f.readline().strip()
#     # print(a[::-1])
#     r=''
#     for i in a:
#         r=i+r
#     print(r)

# f=open('python/dpk2.txt','a')
# f.write('New file using append')


#Letters Count
f=open('python/dpk.txt','r')
l=f.readlines()
f.seek(0)
letter=0
# for i in range(len(l)):
#     a=f.readline().strip()
#     for i in a:
#         if i !=' ':
#             letter+=1
# print(letter)

#count captial and lower
#COUNT THE WORDS
cap=0
word=0
for i in range(len(l)):
    a=f.readline().strip()
    s=a.split(' ')
    for i in s:
        if i!='':
            word+=1
    for i in a:
        if i!=' ':
            if i.isupper():
                cap+=1
            letter+=1

print("Total letters",letter)
print("Capital Letters =",cap)
print("Small Letters =",letter-cap)
print("Total words=",word)
print("No of Lines= ",len(l))








    
    


