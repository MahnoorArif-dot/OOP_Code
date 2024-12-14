#Practice:2
x=int(input('Enter first number:'))
y=int(input('Enter second number:'))
z=int(input('Enter third number:'))
w=(x+y+z)//3
print('Average:',w)

x=int(input('Enter first number:'))
y=int(input('Enter second number:'))
print('Sum:',x+y)
print('Difference:',x-y)
print('Product:',x*y)

a=int(input('Enter Hours:'))
b=a*60
print("Number of minutes:",b)

a=int(input('Enter Seconds:'))
b=a//3600
f=a%3600
c=f//60
d=f%60
print('Number of hours:',b)
print('Number of minutes:',c)
print('Number of seconds:',d)

x=input('Enter any string:')
y=input('Enter any string:')
print('Length of string1=:',len(x))
print('Length of string2=:',len(y))
print('Sum of both length:',len(x)+len(y))
#Practice:3
x = int(input('Enter Biology Marks: '))
y = int(input('Enter Physics Marks: '))
z = int(input('Enter Chemistry Marks: '))
a = int(input('Enter English Marks: '))
b = int(input('Enter Maths Marks: '))
c = int(input('Enter Urdu Marks: '))
d = int(input('Enter Pak studies Marks: '))
e = int(input('Enter Islamiat Marks: '))

w = x + y + z + a + b + c + d + e
percentage = (w / 525) * 100

print('Subject\t\tTotal\tObtained')
print('English\t\t75\t', a)
print('Urdu\t\t75\t', c)
print('Maths\t\t75\t', b)
print('Islamiat\t50\t', e)
print('Pak Studies\t50\t', d)
print('Physics\t\t75\t', y)
print('Chemistry\t75\t', z)
print('Biology\t\t75\t', x)
print('Total\t\t525\t', w)
print('Percentage\t', percentage)

v=int(input('Last Merit Of GC:'))
rm=v-w
print('Required Marks:',rm)

x=int(input('Numerator:'))
y=int(input('Denominator:'))
print('Value:',x/y)
x=int(input('Numerator:'))
y=int(input('Denominator:'))
print('Value:',x/y)
print('Previous Month Budget')
x=int(input('Milk:'))
y=int(input('Sugar:'))
z=int(input('Tea:'))
w=int(input('Biscuit:'))
a=x*0.20
b=y*0.20
c=z*0.20
d=w*0.20
print('Next Month Budget')
print('Milk\t',a+x)
print('Sugar\t',b+y)
print('Tea\t',c+z)
print('Biscuits:',d+w)
print('------------------------')
print('Total:\t',(a+x)+(b+y)+(c+z)+(w+d))
#Practice 4:
from random import*
x=randint(1,10)
print(x)
y=int(input('Guess:'))
if x==y:
    print('You Win!!')
else:
    y=int(input('Guess:'))
    if x==y:
        print('You Win!!')
    else:
        y=int(input('Guess:'))
        if x==y:
            print('You Win!!')
        else:
            print('You Lose!!')
from random import*
x=randint(1,10)
y=randint(1,10)
z=randint(1,10)
print(x,y,z)
if x-y==2 and y-x==2 and y-z==2 and z-y==2 and x-z==2 and z-x==2:
    print('Ok')
else:
    print('Sorry')
        
from random import*
x1 = randint(1, 100000)
x2 = randint(1, 100000)
x3 = randint(1, 100000)
x4 = randint(1, 100000)
print('Numbers before ordering')
print(f'x1:{x1}\tx2:{x2}\tx3:{x3}\tx4:{x4}')
if x1>x2:
    x2,x1=x1,x2
if x2>x3:
    x2,x3=x3,x2
if x3>x4:
    x3,x4=x4,x3
if x1>x2:
    x2,x1=x1,x2
if x2>x3:
    x2,x3=x3,x2
if x1>x2:
    x2,x1=x1,x2
print('Numbers after ordering')
print(f'x1:{x1}\tx2:{x2}\tx3:{x3}\tNx:{x4}')
#Practice 5:
x1=int(input('X1:'))
x2=int(input('X2:'))
y1=int(input('Y1:'))
y2=int(input('Y2:'))
d=(((x2-x1)**2)+((y2-y1)**2))**0.5
print('Distance:',d)

r=int(input('radius:'))
a=(4/3)*(22/7)*((r)**3)
print('Volume:',a)

vi=int(input('initial velociy:'))
acc=int(input('acceleration:'))
ti=int(input('time:'))
dis=int(input('distance:'))
vf=vi+(acc*ti)
vf2=(vi*vi)+(2*acc*dis)
d=(vi*ti)+(0.5*acc*ti**2)
print(f'Final Velocity:{vf}')
print(f'Final Velocity Sq:{vf2}')
print(f'Distance:{d}')

x=int(input('x:'))
y=int(input('y:'))
exp=(x**3)-(y**3)-(3*(x**2)*y)+(3*x*(y**2))
print('Result:',exp)
#Practice 6:
from random import*
x = randint(1, 5)
y = randint(1, 5)
print('First Number:\t', x)
print('Second Number:\t', y)
if x - y <= 1:
    print('Numbers are almost equal')
else:
    print('Numbers are not equal')

from random import *
x = randint(1, 5)
y = randint(1, 5)
print('First Number:', x)
print('Second Number:', y)
if x-y==1 or y-x==1:
    print('Numbers are almost equal')
elif x == y:
    print('Numbers are exactly equal')
else:
    print('Numbers are not equal')

from random import*
mark1 = randint("Marks: ")
if mark1 >= 85:
    print('Grade:A')
elif mark1 >= 80:
    print('Grade:A-')
elif mark1 >= 75:
    print('Grade:B+')
elif mark1 >= 70:
    print('Grade:B')
elif mark1 >= 65:
    print('Grade:B-')
elif mark1 >= 61:
    print('Grade:C+')
elif mark1 >= 58:
    print('Grade:C')
elif mark1 >= 55:
    print('Grade:C-')
elif mark1 >= 55:
    print('Grade:D')
else:
    print('Grade:F')

x = int(input("Eggs: "))
y = x // 6  
if x%6!=0:  
    y+=1
print("Packs:", y)

x1=int(input('Width of first rectangle:'))
x2=int(input('Length of first rectangle:'))
y1=int(input('Width of second rectangle:'))
y2=int(input('length of second rectangle:'))
area1=x1*x2
area2=y1*y2
if area1>area2:
    print('Results:Second Rectangle is smaller')
else:
    print('Results:First Rectangle is larger')
#Practice 7:
from random import*
x1 = randint(1,1000)
x2 = randint(1,1000)
x3 = randint(1,1000)
print('Before:',x1, x2, x3)
if x1>x2:
    x2,x1=x1,x2
if x2>x3:
    x2,x3=x3,x2
if x1>x2:
    x2,x1=x1,x2
print('After:',x1, x2, x3) 

from random import*
x1 = randint(1, 100000)
x2 = randint(1, 100000)
x3 = randint(1, 100000)
x4 = randint(1, 100000)
print('Numbers before ordering')
print(f'x1:{x1}\tx2:{x2}\tx3:{x3}\tx4:{x4}')
if x1>x2:
    x2,x1=x1,x2
if x2>x3:
    x2,x3=x3,x2
if x3>x4:
    x3,x4=x4,x3
if x1>x2:
    x2,x1=x1,x2
if x2>x3:
    x2,x3=x3,x2
if x1>x2:
    x2,x1=x1,x2
print('Numbers after ordering')
print(f'x1:{x1}\tx2:{x2}\tx3:{x3}\tNx:{x4}')

from random import*
x1 = randint(1, 100000)
x2 = randint(1, 100000)
x3 = randint(1, 100000)
print('Numbers:',x1,x2,x3)
if x1>x2>x3 :
    print('Numbers are in Order')
else:
    print('Numbers are not in Order')

mark1 = int(input("Marks 1: "))
mark2 = int(input("Marks2: "))
if mark1 >= 85:
    grade1 = 'A'
elif mark1 >= 80:
    grade1 = 'A-'
elif mark1 >= 75:
    grade1 = 'B+'
elif mark1 >= 70:
    grade1 = 'B'
elif mark1 >= 65:
    grade1 = 'B-'
elif mark1 >= 60:
    grade1 = 'C+'
elif mark1 >= 55:
    grade1 = 'C'
elif mark1 >= 50:
    grade1 = 'C-'
else:
    grade1 = 'F'

if mark2 >= 85:
    grade2 = 'A'
elif mark2 >= 80:
    grade2 = 'A-'
elif mark2 >= 75:
    grade2 = 'B+'
elif mark2 >= 70:
    grade2 = 'B'
elif mark2 >= 65:
    grade2 = 'B-'
elif mark2 >= 60:
    grade2 = 'C+'
elif mark2 >= 55:
    grade2 = 'C'
elif mark2 >= 50:
    grade2 = 'C-'
else:
    grade2 = 'F'

if mark1 == mark2:
    print("SAME")
elif grade1 == grade2:
    print("ALMOST SAME")
else:
    print("DIFFERENT")

x=int(input('Number:'))
if x%2==0 and x%3!=0 and x%5!=0 and x%7!=0:
    print(f'{x} is only divisible by 2')
elif x%2!=0 and x%3==0 and x%5!=0 and x%7!=0:
    print(f'{x} is only divisible by 3')
elif x%2==0 and x%3==0 and x%5!=0 and x%7!=0:
    print(f'{x} is divisible by 2 and 3')
elif x%2==0 and x%3==0 and x%5!=0 and x%7!=0:
    print(f'{x} is divisible by 2 and 3')
elif x%2==0 and x%3!=0 and x%5==0 and x%7!=0:
    print(f'{x} is divisible by 2 and 5')
elif x%2!=0 and x%3==0 and x%5==0 and x%7!=0:
    print(f'{x} is divisible by 5 and 3')
else:
    print(f'{x} is divisible by 7 and 3')
#Practice 8:
x=ord(input('Enter Character:'))
if x&1==1:
    print('Bit 1 is On')
if x&2==2:
    print('Bit 2 is On')
if x&4==4:
    print('Bit 3 is On')
if x&8==8:
    print('Bit 4 is On')
if x&16==16:
    print('Bit 5 is On')
if x&32==32:
    print('Bit 6 is On')
if x&64==64:
    print('Bit 7 is On')
if x&128==128:
    print('Bit 8 is On')
if x&265==256:
    print('Bit 9 is On')

x=ord(input('Enter Character:'))
y=ord(input('Enter Character:'))
w=chr(x)
z=chr(y)
c=0
if x&1==1 and y&1==1:
    c+=1
if x&2==2 and y&2==2:
    c+=1
if x&4==4 and y&4==4:
    c+=1
if x&8==8 and y&8==8:
    c+=1
if x&16==16 and y&16==16:
    c+=1
if x&32==32 and y&32==32:
    c+=1
if x&64==64 and y&64==64:
    c+=1
if x&128==128 and y&128==128:
    c+=1
if x&265==256 and y&265==256:
    c+=1
print(f'In {w} and {z}, {c} bits are same')

x= input("Enter first character: ")
y= input("Enter second character: ")
diff = ord(x) ^ ord(y)
if diff == 0:
    print(f"'{x}' and '{y}' are same")
else:
    print(f"'{y}' and '{y}' are different")

#Practice 9
x=int(input('Enter three-digit number:'))
a=x//100
b=x%100
c=b//10
d=b%10
print(f'First Digit:{a}')
print(f'Second Digit:{c}')
print(f'Third Digit:{d}')

x=int(input('Enter three-digit number:'))
a=x//100
b=x%100
c=b//10
d=b%10
print('Sum of digits',a+c+d) 

from random import*
n=randint(101,999)
print(n)
reverse_number = n % 10                     
first_digit = n // 100
n = n % 100
second_digit = n // 10
reverse_number = reverse_number * 100 + second_digit * 10 + first_digit
print ('Reverse Number:', reverse_number)

#Practice 10:
i=1
while i<=100:
    if i%2==0:
        print(i,end=' ')
    i+=1

x=int(input('Starting Number:'))
y=int(input('Ending Number:'))
while x<=y:
    print(x,end='')
    x+=1

i=1
s=0
while i<=5:
    x=int(input('Enter number:'))
    s+=x
    i+=1
print('Sum:',s)

i=1
max=0
while i<=5:
    x=int(input('Enter number:'))
    if max<x:
        max=x
    i+=1
print('Max:',max)

i=50
while i>=1:
    if i%2!=0:
        print(i,end=' ')
    i-=1
#Practice 11:
from random import*
i=1
while i<=10:
    x=randint(1,10)
    y=randint(1,10)
    print(f'X:{x},Y:{y}')
    if x>y:
        print('First Number is larger')
    else:
        print('Second Number is larger')
    i+=1

from random import*
i=1
while i<=10:
    x1=randint(1,100)
    x2=randint(1,100)
    x3=randint(1,100)
    print(f'Before:\tX1:{x1}\tX2:{x2}\tX3:{x3}')
    if x1>x2:
        x2,x1=x1,x2
    if x2>x3:
        x2,x3=x3,x2
    if x1>x2:
        x2,x1=x1,x2
    print(f'After:\tX1:{x1}\tX2:{x2}\tX3:{x3}')
    print()
    i+=1

from random import*
i = 1
while i <= 10:
    n = randint(1, 100)
    print('Number:', n)
    f = n // 10
    s = n % 10      
    if f == 2:      print('twenty', end=' ')
    elif f == 3:    print('thirty', end=' ')
    elif f == 4:    print('forty', end=' ')
    elif f == 5:    print('fifty', end=' ')
    elif f == 6:    print('sixty', end=' ')
    elif f == 7:    print('seventy', end=' ')
    elif f == 8:    print('eighty', end=' ')
    elif f == 9:    print('ninety', end=' ')

    if n == 10:     print('ten', end='')
    elif n == 11:   print('eleven')
    elif n == 12:   print('twelve')
    elif n == 13:   print('thirteen')
    elif n == 14:   print('fourteen')
    elif n == 15:   print('fifteen')
    elif n == 16:   print('sixteen')
    elif n == 17:   print('seventeen')
    elif n == 18:   print('eighteen')
    elif n == 19:   print('nineteen')
    elif n == 100:   print('hundred', end='')
    elif s == 1:    print('one')
    elif s == 2:    print('two')
    elif s == 3:    print('three')
    elif s == 4:    print('four')
    elif s == 5:    print('five')
    elif s == 6:    print('six')
    elif s == 7:    print('seven')
    elif s == 8:    print('eight')
    elif s == 9:    print('nine')
    if s == 0:      print()
    i = i + 1



from random import*
i=1
while i<=10:
    x=chr(randint(67,90))
    print('Alphabet:\t',x)
    if x=='A' or x=='E' or x=='I' or x=='O' or x=='U':
        print('Alphabet is Vowel')
    else:
        print('Alphabet is consonant')
    i+=1

from random import*
i=1
se=0
so=0
while i<=10:
    x=randint(1,50)
    print('Number:',x)
    if x%2==0:
        se+=x
    else:
        so+=x
    i+=1
print('Sum of even numbers:',se)
print('Sum of odd numbers:',so)

#Practice 12:
x=int(input('Input:'))
a=65
i=1
while i<=x:
    print(chr(a),end='')
    i+=1
    a+=1
print()
a=97
i=1
while i<=x:
    print(chr(a),end='')
    i+=1
    a+=1

x=int(input('Input:'))
a=65
b=122
i=1
while i<=x:
    print(chr(a),end='')
    print(chr(b),end='')
    i+=1
    a+=1
    b-=1

x = int(input("Input:"))
if x%2== 0:  
    i=1
    while i<=x:
        print(i,end=" ")
        i += 1
else:  
    i=x
    while i>=1:
        print(i,end=" ")
        i-=1
#Practice 14:
while i<=100:
    if i%3==0:
        print(i,end=' ')
    i+=1

i=1
while i<=100:
    if i%3==0 or i%5==0:
        print(i,end=' ')
    i+=1

i=1
while i <= 100:
    if (i % 3 == 0) and (i % 5 == 0):
        i += 1
    if (i % 3 == 0) or (i % 5 == 0):
        print(i, end=" ")
    i += 1

i=1
while i<=100:
    print(i,end=' ')
    if i%5==0:
        print()
    i+=1

c = ord('A')
while c <= ord('Z'):
    if chr(c) in 'ADHNT':
        print(chr(c))
    elif chr(c) in 'EIOU':
        print(chr(c))
    else:
        print(chr(c), end=' ')
    c += 1
#Practice 13:
file1 = open('nums.txt', 'r')
i = 1
s = 0
while i <= 1000:
    content = file1.readline()
    s += int(content)
    i += 1

file1.close()

print('Average:', s /1000)

file=open('nums.txt','r')
count=1
a=b=c=d=e=f=g=h=i=0
while count<10000:
    content=file.readline()
    if int(content)==1:
        a+=1
    if int(content)==2:
        b+=1
    if int(content)==3:
        c+=1
    if int(content)==4:
        d+=1
    if int(content)==5:
        e+=1
    if int(content)==6:
        f+=1
    if int(content)==7:
        g+=1
    if int(content)==8:
        h+=1
    if int(content)==9:
        i+=1
    count+=1
file.close()
print(f' count of 1:{a}')
print(f' count of 2:{b}')
print(f' count of 3:{c}')
print(f' count of 4:{d}')
print(f' count of 5:{e}')
print(f' count of 6:{f}')
print(f' count of 7:{g}')
print(f' count of 8:{h}')
print(f' count of 9:{i}')

file=open('nums.txt','r')
count=1
a=b=c=d=e=f=g=h=i=0
while count<10000:
    content=file.readline()
    if int(content)==1:
        a+=1
    if int(content)==2:
        b+=1
    if int(content)==3:
        c+=1
    if int(content)==4:
        d+=1
    if int(content)==5:
        e+=1
    if int(content)==6:
        f+=1
    if int(content)==7:
        g+=1
    if int(content)==8:
        h+=1
    if int(content)==9:
        i+=1
    count+=1
file.close()
file1=open('count.txt','w')
file1.write(str(a)+'\n')
file1.write(str(b)+'\n')
file1.write(str(c)+'\n')
file1.write(str(d)+'\n')
file1.write(str(e)+'\n')
file1.write(str(f)+'\n')
file1.write(str(g)+'\n')
file1.write(str(h)+'\n')
file1.write(str(i)+'\n')
file1.close()

file=open('count.txt','r')
s=0
i=1
while i<=9:
    content=file.readline()
    s+=int(content)
    i+=1
file.close()
print(s)
if s==10000:
    print('File is valid')
else:
    print('File is not valid')

#Practice 14:
i=1
while i<=100:
    if i % 3==0:
        print(i,end=' ')
    i+=1


i=1
while i<=100:
    if i % 3==0 and i%5==0:
        print(i,end=' ')
    i+=1


i=1
while i<=100:
    if (i%3==0 and i%5!=0) or (i % 3!=0 and i%5==0):
        print(i,end=' ')
    i+=1


n1=int(input('N1:'))
n2=int(input('N2:'))
i=s=0
while i<n2:
    if n1<=n2:
        x=n1+i
        print(x,end=' ')
        s+=x
    i+=1
print()
print('Sum:',s)


i=1
while i<=100:
    print(i,end=' ')
    if i%5==0:
        print()
    i+=1

i=1
c=65
while i <= 26:
    x=chr(c)
    print(x,end=' ')
    if x=='A' or x=='D' or x=='H' or x=='N' or x=='T':
        print()
    if  x=='E' or x=='I' or x=='O' or x=='U':
        print()
    c+=1
    i+=1

#Practice 15:
from random import*
i=1
s=0
while i<=10:
    c=0
    x=randint(0,255)
    y=randint(0,255)
    print(f'Number:x {x}\nNumber:y {y}')
    print(f'Character x:{chr(x)} \nCharacter y:{chr(y)}')
    if x&1==1 and y&1==1:
        c+=1
    if x&2==2 and y&2==2:
        c+=1
    if x&4==4 and y&4==4:
        c+=1
    if x&8==8 and y&8==8:
        c+=1
    if x&16==16 and y&16==16:
        c+=1
    if x&32==32 and y&32==32:
        c+=1
    if x&64==64 and y&64==64:
        c+=1
    if x&128==128 and y&128==128:
        c+=1
    s+=c
    i+=1
    print(f'In {x} and {y}: {c} bits are similar')
print(f'TOTAL NUMBER OF BITS:{s}')

    
from random import*
x=randint(1,500)
print(f'Decimal Number:{x}')
print('Octal Number:',end='')
while x>0:
    print(x%8,end='')
    x=x//8

from random import randint
a = []
i = 1
while i <= 10:
    n1 = randint(1, 100)
    n2 = randint(1, 100)
    n3 = randint(1, 100)
    print(f'{n1} {n2} {n3}')
    avg = (n1 + n2 + n3) // 3
    print(f'Average: {avg}')
    a.append(avg)
    i += 1
max= 0
count = 1
b = 0
while b < 10:
    if a[b] >= max:
        max= a[b]
        count= b+1
    b += 1
print(f'Set {count} has the highest average of {max}')


#Practice 17:
x = int(input('N:'))
y = int(input('K:'))
i =1
while i <= x:
    j= 1
    while j <= y:
        print(i,j, end='')
        j += 1
        print()
    i += 1

x=int(input('Rows:'))
y=int(input('Columns:'))
i=1
while i<=x:
    j=1
    while j<=y:
        print(j,end=' ')
        j+=1
    i+=1
    print()

x=int(input('Rows:'))
y=int(input('Columns:'))
i=0
while i<x:
    j=1
    while j<=y:
        print(i+j,end='')
        j+=1
    i+=1
    print()

x=int(input('Rows:'))
y=int(input('columns:'))
i=1
while i<=x:
    j=1
    while j<=x:
        print(' ',end='')
        j+=1
    print(i,end='')
    print()
    i+=1

x=int(input('Rows:'))
i=1
while i<=x:
    j=1
    while j<=i:
        print(' ',end='')
        j+=1
    print(i,end='')
    print()
    i+=1

x=int(input('Rows:'))
y=int(input('Columns:'))
i=1
while i<=x:
    j=1
    while j<=y:
        print(i,end=' ')
        j+=1
    
    print()
    i+=1

x=int(input('Rows:'))
i = 1
while i <= x:
    j = 1
    while j <=x-i:
        print(" ", end="")
        j += 1
    print(i)
    i += 1  

x=int(input('Rows:'))
y=int(input('Columns:'))
i=1
a=97
while i<=x:
    j=1
    while j<=y:
        print(i,end='')
        j+=1
    print()
    k=1
    while k<=y:
        print(chr(a),end='')
        k+=1
    i+=1
    a+=1
    print()

x = int(input('Rows: '))
y = int(input('Columns: '))
i = 1
a = 97
while i <= x:
    j = 0
    while j < y:
        print(i + j, end=' ')
        j += 1
    print()
    k = 0
    while k < y:
        print(chr(a + i - 1 + k), end=' ')
        k += 1
    i += 1
    print()