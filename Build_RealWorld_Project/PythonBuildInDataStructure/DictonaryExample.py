'''
1) Introduction to Dictionary
2) Creating Dictonary
3) Accessing Dictionary
4) Modifying Dictonary
5) Dictionary Methods
6) Iterating Over Dictionary
7) Nexted Dictionary
8) Dictionary Comprehensions
9) Practical Examples
'''


'''
   Dictionary are unordered collection of items, They store data in key-value par.Key must be unique


'''

empty_dict={}
print(empty_dict)
print(type(empty_dict))

# Another way
############### 
empty_dict=dict()
print(empty_dict)

student={"name": "Michael","age": "42","grade": "12"}
print(student)

#Accessing the Dictonary

print(student['grade'])
# OR 
print(student.get('grade'))


# Modifying the Dictonary

student['grade']="123"
print(student)

