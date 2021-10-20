import random
import array 
array=[]
len=int(input())
print('Please enter the array numbers: ')
index=random.randint(0,len(array)-1)
for i in range(index):
  if(array[i]!=array[i+1]):
        print(array)
  else:
         print('repetitive')
         break
   
