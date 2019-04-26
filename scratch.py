#1
def get_sum(n1,n2):
    sum=0
    for i in range(n1,n2+1,1):
        sum+=i

    return sum
sum=get_sum(2,5)
print(sum)

#2
count = 0
def inc(n):
    for i in range(n):
        count+=1

    return count

n=int(input("관람객 수 : "))
print(inc(n))

#3
def get_max(a,b):
    if a>b:
        return a
    else:
        return b

def get_min(a,b):
    if a>b:
        return b
    else:
        return a

x=int(input("source : "))
y=int(input("dest : "))

dist=get_max(x,y)-get_min(x,y)
print("distance : %d " %dist)

#4
def count_up(n1,n2):

    for i in range(n1+1,n2,1):
        print(i)

count_up(1,5)

#5
def get_filtered(data,filter):
    newX=''
    for letter in data:
        if letter not in filter:
            newX+=letter

    return newX

x=input("문장을 입력하시오 : ")
y="'?$#!_-."

print(get_filtered(x,y))

#6
def bin_to_dec(bin):
    bin_len=len(bin)
    dec=0
    for i in range(bin_len):
        if bin[i]=='1':
            dec+=2**(bin_len-1-i)
    return dec

n1=input("2진수 : ")
print("10진수 : %d" %(bin_to_dec(n1)))
