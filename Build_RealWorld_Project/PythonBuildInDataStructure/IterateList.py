number=[1,2,3,4,5,6,7,8,9,10]

#for number in number:
#    print(number)

# Getting the values with Index : 
#for index,number in enumerate(number):
#    print(index,number)

### LIST Comprehenion

lst=[]
for x in range(10):
    lst.append(x**2)

#print(lst)


even_number=[num **2 for num in range(10) if num%2==0]
#print(even_number)


### Nested List

lst1=[1,2,3,4]
lst2=['a','b','c','d']

pair= [[i,j]for i in lst1 for j in lst2]

#print(pair)


# List Comprehension with function calls

words=["hello","world","python","list","Computer"]

lengths=[len(word) for word in words]

print(lengths)