import math
import random

# methods for RSA keys 
def genKey():
    #Choose two distinct primes, p and q
    p = random.randint(2, 1000)
    q = random.randint(2, 1000)
    
    #Test if p and q are prime
    while not Fermat(p):
        if not Fermat(p):
            p = random.randint(2, 1000)
    
    while not Fermat(q):
        if not Fermat(q):
            q = random.randint(2, 1000)
            
    #Compute n = pq
    n = p * q
    
    #Compute phi = (p-1)(q-1)
    phi = (p - 1) * (q - 1)
    
    #Choose e such that 1 < e < phi and e and phi are coprime
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        if gcd(e, phi) != 1:
            e = random.randint(2, phi - 1)
    
    #Find a d where ed is identical to 1 (mod phi)
    d = random.randint(2, phi - 1)
    while (e*d) % phi != 1:
        if (e*d) % phi != 1:
            d = random.randint(2, phi - 1)
    
    return n, e, d
    
def Fermat(p = 137):
    '''Test if p is prime with Fermat\'s little theorem\n'''
    t = True
    for i in range(1, p):
        if pow(i, p-1, p) != 1:
            t = False
            break
    if not t:
        return False
    else:
        return True
    
def gcd(a=1, b=1):
    ''' The gcd function implements Euclid's
    GCD algorithm to find the greatest common
    divisor of two positive integers a and b'''
    
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

genKey()
   

# methods for encryption and decryption 
def encrypt(message, N, e): # you use public key for encryption 
   # need to convert to ascii 
   encrypted_message = pow(message, e, N)
   # turn the message back into a string to return the message 
   # when you encrypt the message it should be all integers 
   return encrypted_message
   
def decrypt(encypted_message, N, d): # use private key to decrypt
   # comvert the encrypted message which is in all integers 
   # back into ascii characters in order to return the original message 
   decrypted_message = pow(encypted_message, d, N)
   # turn it back into a string to return the message 
   return decrypted_message


# methods for authentications 

def sign(message, private_key): # sign a message using a private key
   n, d = private_key
   signature = pow(message, d, n)
   return signature

def verify(message, signature, public_key): # verify a signature using a public key
   n, e = public_key
   decrypted_signature = pow(signature, e, n)
   return decrypted_signature == message


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
                   #   check if theres a message to authenticate 
                   if len(signatures) == 0:
                     print("There are no messages to authenticate")
                   else:
                      print("The following messages are available: ")
                   # for i in range(len(signatures):
                   #       print(i, ".", signatures[i], end = "\n")
                      signature = sign(message, private_key)
                      print("Signature: ", signature)           
                     #valid = input("Enter your choice")
                     # checking to see if its valid or not
                      verified = verify(message, signature, public_key)
                      print("Verified: ", verified)
                                   
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
            
