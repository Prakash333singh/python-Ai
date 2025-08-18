student = {
    "name":"Prakash",
    "age":21,
    "is_student":True
}

print(student['name'])
student['age']=22;
student['grade']="A"

print(student)


x='100'
print(int(x))
print(float(x))
print(str(x)) 


sentence = "Learning Python is Fun"
print(sentence[0])
print(sentence[-1])
print(sentence[11])
print(len(sentence))
#how to access middle character
middle_index = len(sentence) //2
print(sentence[middle_index])  # Accessing the middle character

#extact python from sentence
start_index = sentence.index("Python")  
end_index = start_index + len("Python")
extracted_word = sentence[start_index:end_index]
print(extracted_word)  # Output: Python