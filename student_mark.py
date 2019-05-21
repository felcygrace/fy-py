list_of_marks=(12,18,25,24,2,5,18,20,20,21)

def find_more_than_average():
    count=0 
    for i in list_of_marks:
        if i>12:
            count+=1
            find_more_than_average=(count/10)*100
            
    return find_more_than_average
def sort_marks():
    sort_marks=list(sorted(list_of_marks))
    return sort_marks
def generate_frequency():
    list1=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    list2=sort_marks
    generate_frequency=[]
    count=0
    for i in list1:
        if(list1[i]==list2[i]):
            generate_frequency.append(count)
            count+=1
            return generate_frequency
        else:
            return 0

print(find_more_than_average())
print(generate_frequency())
print(sort_marks())
