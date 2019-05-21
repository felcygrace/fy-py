def display(num):
    message=""
    if num%5==0 and num%3==0:
        print("zoom")
    elif num%5==0:
        print("zap")
    elif num%3==0:
        print("zip")
    else:
        print("invalid")
    #write your logic here
    return message

#Provide different values for num and test your program
message=display(10)
print(message)
