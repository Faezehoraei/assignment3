a = int (input('enter a : '))
b = int (input('enter b : '))
bmm=1
for i in range(1,min(a,b)+1,1):
    if((a%i==0)and(b%i==0)):
        bmm=i
print('BMM =',bmm)