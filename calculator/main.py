import numbers
from add import add
from sub import sub
from mul import mul
from div import div
from mod import mod
# from numbers import num
while True:
    print("""
          1.Add
          2.Substrction
          3.Multiplication
          4.Division
          5.mod
          6.Exist
          """)
    choice=int(input("Enter ur Choices ::"))
    
    if choice==1:
        a,b=numbers.num()
        add(a,b)
    elif choice==2:
        a,b=numbers.num()
        sub(a,b)
    elif choice==3:
        a,b=numbers.num()
        mul(a,b)
    elif choice==4:
        a,b=numbers.num()
        div(a,b)
    elif choice==5:
        a,b=numbers.num()
        mod(a,b)
    elif choice==6:
        break
    else :
        print("Invalid choices ")