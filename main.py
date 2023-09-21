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
   
# functions to encrypt the message
def encrypt_message(message, N, e): 
   ''' Function uses public key to encrypt the message '''
   encrypted_message = []
   
   for char in message: 
      char = ord(char)
      encrypted_char = encrypt(char, N, e)
      encrypted_message.append(encrypted_char)
      
   return encrypted_message

def encrypt(char, N, e):
   ''' encrypt each character'''
   return pow(char, e, N)

# functions to decrypt the message
def decrypted_message(encrypted_message, N, d):
   ''' Function uses private key to decrypt the encrypted message'''
   message = []
   
   for char in encrypted_message:
      decrypted_char = decrypt(char, N, d)
      message.append(decrypted_char)
      
   decrypted_message = ''.join([chr(i) for i in message])
  
   return decrypted_message

def decrypt(char, N, d):
   ''' decrypt each character'''
   return pow(char, d, N)
 

# methods for authentications 
def sign(message, d, N): # sign a message using a private key
   #n, d = private_key
   signature = pow(message, d, N)
   return signature

def verify(message, signature, N, e): # verify a signature using a public key
   #n, e = public_key
   decrypted_signature = pow(signature, e, N)
   return decrypted_signature == message


# create a list that will hold all of the messages that are encrypted 
encrypted_messages = []
# create a list that will hold all of the signatures 
signatures = []

print("\nRSA keys have been generated.")
# generate the RSA keys here 
N, e, d = genKey()


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
                     emessage = encrypt_message(message, N, e)
                     # store the message in the list 
                     encrypted_messages.append(emessage)
                     print("Message encrypted and sent")
                     print()
                  elif(choice == "2"):
                   #   check if theres a message to authenticate 
                   if len(signatures) == 0:
                     print("There are no messages to authenticate")
                   else:
                      print("The following messages are available: ")
                      for i in range(len(signatures)):
                          print(i, ".", len(signatures[i]), end = "\n")
                      #signature = sign(message, private_key)
                      #print("Signature: ", signature)           
                      valid = input("Enter your choice")
                     # checking to see if its valid or not
                      #verified = verify(message, signature, public_key)
                      #print("Verified: ", verified)
                      if (valid <= len(signatures)):
                         print("Signature is valid")
                                   
                      print()
                  else:
                     break
        
        elif(user_type == "2"):  
            while True:        
                   choice = input("As owners of the keys, what would you like to do?\n1. Decrypt a reciever message\n2. Digitally sign a message\n3. Show the keys\n4. Generate a new set of keys\n5. Exit\nEnter your choice:")

                   if (choice == "1"):
                     if len(encrypted_messages) == 0:
                         print("There are no messages to decrypt")
                     else:
                        print("The following messages are available:")
                        for i in range(len(encrypted_messages)):
                             print(i + 1, ". (length =", len(encrypted_messages[i]), ')', end ="\n")
                        valid = input("Enter your choice: ")
                        # add checking to see if its valid or not later
                        if (int(valid) <= len(encrypted_messages)):
                            print("Decrypted message:", decrypted_message(encrypted_messages[int(valid) -1 ], N, d))
                     print()
                   elif (choice == "2"):
                     signature = input("Enter signature: ")
                     #signatures.append(signature)
                     print("Message signed and sent")
                     print()
                   elif (choice == "3"):
                     # show the keys
                     print(f"Private key is: N = {N}, d = {d}")
                     print(f"Public key is: N = {N}, e = {e}")
                     print()
                   elif (choice == "4"):
                     # generate the new keys
                     N, e, d = genKey()
                     print("New keys have been generated")
                     print()
                   else: 
                     break
                  
        else:
            print("Bye for now")
            break
            
