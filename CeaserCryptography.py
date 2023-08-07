
print("Welcome to the world of cryptography")

def main():
    print()
    print("Choose one option")
    choice = int(input("1. Encryption\n2. Decryption\nChoose(1,2): "))
    if choice == 1:
        encryption()
    elif choice == 2:
        decryption()
    else:
        print("Wrong Choice")


def encryption():
    print("encryption")
    msg=input("enter your message: ")
    key=int(input("enter key(1-94): "))
    encryptedText=""
    for i in range(len(msg)):
        temp=(ord(msg[i])+key)
        if(temp>126):
            temp=temp-127+32
        encryptedText+=chr(temp)
    print("encrypted: "+encryptedText)
    main()

def decryption():
    print("decryption")
    encryptmsg=input("enter encrypted text: ")
    decryptedkey=int(input("enter key(1-94): "))
    decryptedText=""
    for i in range(len(encryptmsg)):
        temp=(ord(encryptmsg[i])-decryptedkey)
        if(temp<32):
            temp=temp+127-32
        decryptedText+=chr(temp)
    print("decrypted: "+decryptedText)
    
      
if __name__ == "__main__":
    main()
