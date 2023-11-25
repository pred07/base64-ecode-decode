import base64

def encrypt_pass(password):
    encode_bytes = base64.b64encode(password.encode())
    print(encode_bytes)

def decrypt_pass(password):
    decode_bytes = base64.b64decode(password)
    decode_data = decode_bytes.decode()
    
    print(decode_data)

command = input("DECODE or ENCODE: ").lower()
user_pass = input("Enter the string: ")

if(command == "encode"):
    encrypt_pass(user_pass)
elif(command == "decode"):
    decrypt_pass(user_pass)
else:
    print("Invalid Command !")