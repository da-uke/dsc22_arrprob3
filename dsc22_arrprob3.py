from array import array
a=array('i',[1,1,0,0,1,1,1,0,1,1,0,1,1,1,1,0,0,3,1,1,1,1,1,1,1,1,0,1])
n=len(a)
count=0
final=0
for i in range(n):
    if a[i]==0:
        count=0
    else:
        count+=1
        if count>final:
            final=count
    print(final)
y0=0
for i in range(n):
    if a[i]!=0:
        a[i],a[y0]=a[y0],a[i]
        y0+=1
for i in range(n):
    print(a[i] ,end=" ")
arr=array('i',[6,9,2,3,7,4,3,7,5,3])
minel=9999
maxel=0
l=len(arr)
for i in range(l):
    if arr[i]<minel:
        minel=arr[i]
    elif arr[i]>maxel:
        maxel=arr[i]
print("\n",maxel-minel ,minel,maxel)

