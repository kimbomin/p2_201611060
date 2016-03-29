
# coding: utf-8

# In[1]:

import turtle


# In[4]:

wn=turtle.Screen()


# In[6]:

t1=turtle.Turtle()


# In[7]:

def makebaramgaebi(size,bigger,sides,angle):
    for i in range(0,sides):
        if(i%2):
            size=size+bigger
            t1.fd(size)
            t1.right(90)
            
makebaramgaebi(30,30,40,110)

wn.exitonclick()


# In[ ]:



