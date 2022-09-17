#!/usr/bin/env python
# coding: utf-8

# Q1) Which of the following operators is used to calculate remainder in a division?
# 
# Option (C) - %
# 
# 
# Q2) In python 2//3 is equal to? 
# 
# Option (A) - 0.6666
# 
# Q3) In python, 6<<2 is equal to?
# 
# Option (C) - 24
# Q4) In python, 6&2 will give which of the following as output?
# 
# Option (A) - 2
# 
# Q5) In python, 6|2 will give which of the following as output?
# 
# Option (D) - 6
# 
# Q6) What does the finally keyword denotes in python?
# 
# Option (C) - the finally block will be executed no matter if the try block raises an error or not.
# 
# Q7) What does raise keyword is used for in python?
# 
# Option (A) - It is used to raise an exception.
# 
# Q8) Which of the following is a common use case of yield keyword in python?
# 
# Option (C) - in defining an iterator
# 
# Q9) Which of the following are the valid variable names?
# 
# Options A and C
# 
# Q10) Which of the following are the keywords in python?
# 
# Options A and B

# Q11) Write a python program to find the factorial of a number?

# In[1]:


factorial = 1
num  = int(input('Enter a number:  '))

if num == 0:
    print("The factorial of 0 is 1")
    
else:
    
    for i in range(1,num + 1):
        
        factorial = factorial*i
        
print("The factorial of",num,"is",factorial)


# Q12) Write a python program to find whether a number is prime or composite.

# In[2]:


n= int(input("Enter any number:"))
if(n ==0 or n == 1):
    printf(n," is neither prime nor composite")
elif n>1 :
    for i in range(2,n):
        if(n%i == 0):
            print(n,"is a composite number")
            break
    else:
        print(n," is a prime  number")
else :
    print("Please enter positive number only ")


# Q13) Write a python program to check whether a given string is              palindrome or not.
# 

# In[3]:


string=input(("Enter a string:")).upper() # to remove case sensitivity from input string


if(string==string[::-1]):
      print(string,"is a palindrome")
else:
      print(string,"is not a palindrome")
  


# Q14) Write a Python program to get the third side of right-angled triangle from two given sides.

# In[5]:


def rightangledtriangle(a,b,c):
        if a == str("x"):
            return ("a = " + str(((c**2) - (b**2))**0.5))
        elif b == str("x"):
            return ("b = " + str(((c**2) - (a**2))**0.5))
        elif c == str("x"):
            return ("c = " + str(((a**2) + (b**2))**0.5))
        else:
            return 'Nothing'


# In[6]:


print(rightangledtriangle(3,4,'x'))


# In[7]:


print(rightangledtriangle(3,'x',4))


# Q15) Write a python program to print the frequency of each of the characters present in a given string

# In[8]:


def stringchar(s):
    
    all_freq = {}
  
    for i in s:
    
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    print("Count of all characters in",s,":\n "+ str(all_freq))
  


# In[9]:


stringchar('Misiisipi')


# In[ ]:




