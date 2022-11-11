#SELECTION SORT
size=int(input("Enter size of list:"))
a=[]
for i in range (size):
    val=int(input("Enter No:"))
    a.append(val)

for i in range(size):
    min=i #पहिल्या element ला min समजले
    for j in range (i+1,size):#i+1होऊनsizeपर्यंत.चालणार
        if (a[j]<a[min]):#जर min मोठा असेल
            min=j    #min j
            t=a[i]     #temp मध्ये i
            a[i]=a[min] #swap करण्यासाठी
            a[min]=t    #min ची वैल्यू temp मध्ये टाकने
print("Sorted list is :")
print(a)