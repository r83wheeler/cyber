#decode

#initializing string
str = "secret phrase".encode('utf-8')

#printing the encoded string
print("The encoded string in base64 format is: ",)
print("b from bytes", str, "\n")

#printing the original decoded string
print("The decoded string is: ",)
print(str.decode('utf-8', 'string'))

