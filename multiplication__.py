f=open('python/dpk2.txt','a')

m=int(input("Enter a multiplication :"))
# i=1
# for i in range(i,10+1):
    # b=i,"*",m,"=",i*m
    # b=str(b)
    # f.write(b)
    # f.write(str(i)+'*'+str(m)+'='+str(i*m)+'\n')


for i in range(1,11):
    for j in range(1,m+1):
        f.write(str(i)+'*'+str(j)+'='+str(i*j)+'\t')
    f.write('\n')


    

