a = input("Enter your first name: ")

myfile = open("Samuj.txt", "w", encoding="utf-8")    
myfile.write(a)
myfile.close()
print("File created and data written successfully.")

myfile = open("Samuj.txt", "r", encoding="UTF-8")
content = myfile.read() # Reads everything you just saved [2]
print("Content of the file:", content)
myfile.close()
