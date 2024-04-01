def AandB(a, b):

    result = ""
    while a>0 or b>0 :
        if result[-2:] != "AA" and a>b:
            result+="A"
            a=a-1
        elif result[-2:] == "AA":
            result+="B"
            b=b-1
        elif a>b:
            result+="A"
            a=a-1
        elif a==b:
            result+="A"
            a=a-1
        else : 
            result+="B"
            b=b-1
    print(result)


# รับ input จากผู้ใช้
a = int(input("input number of A: "))
b = int(input("input number of B: "))

if(a<b) : print("error")

else :AandB(a, b)