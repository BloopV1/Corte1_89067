n = int( input ("Ingese la cantidad de nuemros "))
a = 0 
b = 1 
print (a,"\n",b)
for i in range (n-2):
    c=a+b
    a=b
    b=c
    print(c)


###################################################################################
###################################################################################
###################################################################################

num=int(input("especifique la cantidad de numeros"))
j=2;x=0;n=2
print("1")
while x <= num-2:
    div=n%j
    if div== 0:
        if n==j:
            print(n,end=",")
            x+1= 1
        j = 2
        n+=1
    else: 