# num={}
# n=int(input("Enter a Number :"))
# i=0
# for i in range(n+1):
#     print(i)
#     num[i]=i*i
# print(num)

num={}
n=int(input("Enter a Number :"))
i=0
for i in range(n+1):
    if i%2==0:
        num[i]=i*i
    else :
        num[i]=i*i*i
print(num)
    
    