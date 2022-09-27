#Program-3
# With a single integer as the input, generate the following until a = x [series of numbers as shown in below examples]


a=int(input('a='))            #taking input of count from user
if a%2==0:                           #to check if count is even  
    for i in range(1,(a-1)*2,2):    
        print(str(i),end=",")
else:
    for i in range(1,a*2,2):
        print(str(i),end=",")
