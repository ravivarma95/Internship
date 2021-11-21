#!/usr/bin/env python
# coding: utf-8

# #                                  PYTHON – WORKSHEET 1 
# 
# ## 1 to Q8 have only one correct answer. Choose the correct option to answer your question. 
# 
#  
# 
# 1. Which of the following operators is used to calculate remainder in a division? 
# 
#  Answer: C 
# 
#  A) #  B) &  C) %  D) $
# 
# 
#  2. In python 2//3 is equal to? 
#  
#  Answer:B  
# 
#   A) 0.666  B) 0  C) 1  D) 0.67 
# 
# 3. In python, 6<<2 is equal to? 
# 
#  Answer: C 
# 
#   A) 36  B) 10  C) 24  D) 45 
# 
# 
# 4. In python, 6&2 will give which of the following as output?
# 
#  Answer: A 
# 
#   A) 2  B) True  C) False  D) 0 
#   
# 
# 5. In python, 6|2 will give which of the following as output?
#  
#  Answer: D 
# 
#   A) 2   B) 4   C) 0   D) 6 
# 
# 
# 6. What does the finally keyword denotes in python?
#  
#  Answer: C 
# 
#   A) It is used to mark the end of the code 
# 
#   B) It encloses the lines of code which will be executed if any error occurs while executing the lines of code in the try block. 
# 
#   C) the finally block will be executed no matter if the try block raises an error or not. 
# 
#   D) None of the above 
# 
#  
# 
# 7. What does raise keyword is used for in python? 
# 
#  Answer: A 
# 
#  A) It is used to raise an exception.    B) It is used to define lambda function 
# 
#  C) it's not a keyword in python.	 D) None of the above 
# 
#  
# 
# 8.	Which of the following is a common use case of yield keyword in python?
#  
#  Answer: C 
# 
#  A) in defining an iterator	  B) while defining a lambda function 
# 
#  C) in defining a generator	  D) in for loop.
#  
#   
# 
#  

# ## Q9 and Q10 have multiple correct answers. Choose all the correct options to answer your question. 
# 
#  
# 
# 9.	Which of the following are the valid variable names? 
# 
#  Answer: A& C 
# 
#   A) _abc	B) 1abc 
# 
#   C) abc2	D) None of the above 
# 
#  
# 
# 10. Which of the following are the keywords in python?
# 
#  Answer: A & B 
# 
#   A) yield	B) raise 
# 
#   C) look-in D) all of the above 

# In[11]:


# 11) python program to find the factorial of a number

num=int(input("Enter any number to find factorial: "))

def factorial(X):
    fact=1
    for i in range(1, X+1):
        fact=fact*i
    return fact    

result=factorial(num)

print('The factorial of %d = %d' %(num,result))


# In[9]:


# 12) python program to find whether a number is prime or composite


num = int(input("Enter any number : "))
if num < 2:
    print(num, "is a neither prime NOR composite number")
else:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is NOT a primr number,it is a COMPOSITE number")
            break
    else: 
        print(num, "is a primr number")
        
 


# In[8]:


# 13)  python program to check whether a given string is palindrome or not

strng = input("Enter any number : ")
rev_strng = str(strng)[::-1]
if strng == rev_strng:
    print(strng, "is a palindrome")
else:
    print(strng, "is not a palindrome ")


# In[5]:


#  14) Python program to get the third side of right-angled triangle from two given sides


def pythagoras(opp_side,adj_side,hypo):
        if opp_side == str("x"):
            return ("Opposite = " + str(((hypo**2) - (adj_side**2))**0.5))
        elif adj_side == str("x"):
            return ("Adjacent = " + str(((hypo**2) - (opp_side**2))**0.5))
        elif hypo == str("x"):
            return ("Hypotenuse = " + str(((opp_side**2) + (adj_side**2))**0.5))
        else:
            return "All three sides are given"
        


# In[6]:


print(pythagoras(3,4,'x'))


# In[7]:


print(pythagoras(3,4,10))


# In[14]:


#  15) python program to print the frequency of each of the characters present in a given string

import collections

test_str = str(input("Enter any string : "))

str_count = collections.Counter(test_str)
  
print ("frequency of each of the characters in a given string is : " +  str(str_count))


# In[ ]:




