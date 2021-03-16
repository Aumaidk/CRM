userName = input("Enter Your User Name")
demo = userName.split("@")[0]
helper = int(65)
# encryptedDemo = ""
# for letter in demo:
#     encryptedDemo += "$%s@" % letter
# print(encryptedDemo)

# Python program to move every character  
# K times ahead in a given string  
  
# Function to move string character 
def encode(s, k): 
      
    # changed string  
    newS = "" 
      
    # iterate for every characters 
    for i in range(len(s)):  
          
        # ASCII value  
        val = ord(s[i])  
          
        # store the duplicate  
        dup = k  
          
        # if k-th ahead character exceed 'z'  
        if val + k>122:  
            k -= (122-val)  
            k = k % 26
            newS += chr(96 + k)  
              
        else:  
            newS += chr(val + k)  
          
        k = dup  
      
    # print the new string  
    print (newS)  
              
# driver code      

encode(demo, helper) 