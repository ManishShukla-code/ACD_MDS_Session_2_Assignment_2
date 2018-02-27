
# coding: utf-8

# In[16]:


for i in range(1,10):
    
    for j in range(10-i,0,-1):
        
        if(i<=j):
            print('*'*i)
           # print('i'+str(i))
            break
        else:
                print('*'*j)
            #    print('j'+str(j))
                break
    

    
   


# In[2]:


print('*')

