def reverse(num):
    reverse= 0
    while num:
        reverse= reverse*10 + num%10
        num= num//10
    return reverse

num= 12300
if num==reverse(num):
    print (num)
else:
    while True:
        num+= 1
        if num==reverse(num):
            print (num)
            break
