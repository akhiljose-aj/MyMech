'''start=int(input('starting no'))
end=int(input('ending no'))
sum=0
odd=0
even=0
while start<=end:
    sum+=start
    if start%2==0:
        even+=start
    else:
        odd+=odd
    start+=1

print('sum of natural numbers:',sum)
print('sum of even numbers:',sum)
print('sum of odd numbers:',sum)'''



'''num=int(input("enter a  number"))
sum=0
while num>0:
    digit=num%10
    sum=sum+digit
    num=num//10
print('sum is:',sum)'''


'''num=int(input("enter a number"))
reverse=0
while num>0:
    digit=num%10
    reverse=reverse*10+digit   
    num=num//10
print('the reverse of th number is:',reverse)'''

s=input('enter the string')
rev=''
l=len(s)
i=0
while i<l:
     rev=s[i]+rev
     i+=1
print('reverse is )




