def find_duplicates(list_of_numbers):
    a=len(list_of_numbers)
    repeated = [] 
    for i in range(a): 
        k = i + 1
        for j in range(k, a): 
            if list_of_numbers[i] == list_of_numbers[j] and list_of_numbers[i] not in repeated:
                
                repeated.append(list_of_numbers[i]) 
    
    return repeated #start writing your code here

list_of_numbers=[1,2,2,3,3,3,4,4,4,4]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)
