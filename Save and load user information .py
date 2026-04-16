##

a = input("Enter your first name: ")

myfile = open("Samuj.txt", "w", encoding="utf-8")    
myfile.write(a)
myfile.close()
print("File created and data written successfully.")

myfile = open("Samuj.txt", "r", encoding="UTF-8")
content = myfile.read() # Reads everything you just saved [2]
print("Content of the file:", content)
myfile.close()

##
#Input
a = input("Enter a number: ")

file_interger = open("integer.txt", "w")
file_float = open("float.txt", "w")



#Output
if a.find(",") >= 0:
    file_float = open("float.txt", "w")
    print("Saving successful.")
    print("The number is a float.")
    file_float.close()
else:
    file_interger = open("integer.txt", "w")
    print("Saving successful.")
    print("The number is an integer.")
    file_interger.close()

    if file_interger.closed:
        file_interger = open("integer.txt", "r")
        print("The number", a, "is an integer.")  
    else:
        file_float = open("float.txt", "r")
        print("The number", a, "is a float.")

