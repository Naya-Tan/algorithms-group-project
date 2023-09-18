# methods for RSA keys 
def public_key():
   # create the public key
   # return n and e 
   print()
   
def private_key():
   # create the public key 
   # return e and d 
   print()
   

# methods for encryption and decryption 
def encrypt(message, N, e): # you use public key for encryption 
   # need to convert to ascii 
   encrypted_message = pow(message, e, N)
   # turn the message back into a string to return the message 
   return encrypted_message
   
def decrypt(encypted_message, N, d): # use private key to decrypt
   # need to convert to ascii 
   decrypted_message = pow(encypted_message, d, N)
   # turn it back into a string to return the message 
   return decrypted_message


# methods for authentications 





# create a list that will hold all of the messages that are encrypted 
encrypted_messages = []
# create a list that will hold all of the signatures 
signatures = []

print("\nRSA keys have been generated.")
# generate the RSA keys here 

while True:
        print()
        user_type = input("Please select your user type:\n1. A public user\n2. The owner of the keys\n3. Exit program\nEnter your choice: ")
        print()
   
        if(user_type == "1"):
            while True:
                  choice = input("As a public user, what would you like to do?\n1. Send an encrypted message\n2. Authenticate a digital signature\n3. Exit\nEnter your choice: ")
            
                  if(choice == "1"):
                     message = input("Enter a message: ")
                     # pass message into the encrypt function 
                     # store the message in the list encrypted_messages.append(message)
                     print("Message encrypted and sent")
                     print()
                  elif(choice == "2"):
                  # check if theres a message to authenticate 
                  # if len(signatures) == 0:
                  #   print("There are no messages to authenticate")
                  # else:
                  #    print("The following messages are available: ")
                  #    for i in range(len(signatures):
                  #         print(i, ".", signatures[i], end = "\n")
                  #   valid = input("Enter your choice")
                  #   # add checking to see if its valid or not later
                     print()
                  else:
                     break
        
        elif(user_type == "2"):  
            while True:        
                   choice = input("As owners of the keys, what would you like to do?\n1. Decrypt a reciever message\n2. Digitally sign a message\n3. Show the keys\n4. Generate a new set of keys\n5. Exit\nEnter your choice:")

                   if (choice == "1"):
                     # if len(encypted_messages) == 0:
                     #     print("There are no messages to decrypt")
                     # else:
                     #    print("The following messages are available:")
                     #    for i in range(len(encrypted_messages)):
                     #        print(i, ".", encrypted_messages[i], end ="\n")
                     #     valid = input("Enter your choice: ")
                     #     # add checking to see if its valid or not later
                     #     # print("Decrypted message: ", decrypt(encrypted_messages[int(valid)]))
                     print()
                   elif (choice == "2"):
                     signature = input("Enter signature: ")
                     #signatures.append(signature)
                     print("Message signed and sent")
                     print()
                   elif (choice == "3"):
                     # print("Private key is: ")
                     # print("Public key is: ")
                     print()
                   elif (choice == "4"):
                     # generate a new public key 
                     # generate a new private key 
                     # print("New keys have been generated")
                     print()
                   else: 
                     break
                  
        else:
            print("Bye for now")
            break
            
