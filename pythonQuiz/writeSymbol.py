def symbolPattern(input):
    for i in range(input):
        pattern = ""
        for j in range(input):
            if i==j or i+j== input-1:
                pattern += "*"
            else : pattern += "-"
        print(pattern)
    


input = int(input("Enter odd numbers: "))

if(input%2==0) : print("please input odd number")
else :symbolPattern(input)
