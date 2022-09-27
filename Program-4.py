#Program 4
# Get the total count of number list in the dictionary which is multiple of [1,2,3,4,5,6,7,8,9]



lst=[1,2,3,4,5,6,7,8,9]     #list of numbers to find multiple
#inp=[1,2,8,9,12,46,76,82,15,20,30]   #eg input(hard coding)
inp=[]    #input list
inp=[int(item) for item in input("Enter list item: ").split()]  
opt=[]    #output list
count=0    #to store count of multiples
for i in lst:
    for j in inp:
        if j%i==0:
            count+=1
    opt.append(count)    #adding the count to output list
    count=0
res=dict(zip(lst,opt))    #converting 2 list to dictionary
print(res)
    

            
            
