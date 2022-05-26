from cryptography.fernet import Fernet
import os
import base64
import sys

def generate_key():
    #key=Fernet.generate_key()
    key=base64.urlsafe_b64encode(os.urandom(32))
    with open("key.enc","wb") as file:
        file.write(key)

def load_key():

    return open("key.enc","rb").read()

def encode_msg(message:str):

    key=load_key()
    encoded_msg=message.encode()
    fernet=Fernet(key)
    final_encoded_msg=fernet.encrypt(encoded_msg)
    return final_encoded_msg



def decode_msg(msg):
    key=load_key()
    fernet=Fernet(key)
    decoded_msg=fernet.decrypt(msg)
    return decoded_msg


# #################################################
def encode_file(src:str):
    orginal_str=''
    result=''
    key=load_key()
    fernet=Fernet(key)
    with open(src,'rb') as file:
        orginal_str=file.read()
    result=fernet.encrypt(orginal_str)
    with open(src,'wb') as file:
        file.write(result)
    
    print("Encryption Is Done Successfuly!")

def decode_file(src:str):
    orginal_str=''
    result=''
    key=load_key()
    fernet=Fernet(key)
    with open(src,'rb') as file:
        orginal_str=file.read()
    result=fernet.decrypt(orginal_str)
    with open(src,'wb') as file:
        file.write(result)
    
    print("Decryption Is Done Successfuly!")


if __name__ == "__main__":
    # generate_key()
    # msg=encode_msg("Hello Moein Sarvi")
    # print(msg.decode())
    # plain_text=decode_msg(msg)
    # print(plain_text.decode())
    # encode_file(sys.argv[1])
    decode_file(sys.argv[1])

