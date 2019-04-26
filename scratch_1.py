
'''
mylist=[1,2,3,4,5,6]
print(mylist[0])
print(mylist[1:6])
a=max(mylist)
print(a)
b=min(mylist)
print(b)
sum=0
for i in range(6):
    sum+=mylist[i]
print(sum)
print(mylist[-2])

shopping_list=['apple','bluberry','peach']
print(shopping_list)
shopping_list.append('melon')
print(shopping_list)
shopping_list.remove('melon')
print(shopping_list)
shopping_list.insert(0,'melon')
print(shopping_list)
shopping_list.remove('apple')
print(shopping_list)
shopping_list.pop(1)
print(shopping_list)

customer=[]
for i in range(5):
    customer.append((input('이름을 알려주세요:')))
customer.sort()
print(customer)

customer=[]
for i in range(5):
    customer.append((input('이름을 알려주세요:')))
customer.sort()
customer.reverse()
reverse_list=customer
print(reverse_list)

customer=[]
for i in range(5):
    customer.append((input('이름을 알려주세요:')))
revers_list=[]
for l in range(5):
    revers_list.append(customer[-(l+1)])
print(revers_list)

scores=[]
for i in range(5):
    scores.append(int(input('점수를 말하시오:')))
n=(scores[0]+scores[1]+scores[2]+scores[3]+scores[4])/5
print('성적의 평균은 %.1f입니다'%n)
studentnum=0
for i in range(5):
    if scores[i]>=n:
        studentnum+=1
print('평균 이상의 학생은 %d명 입니다'%studentnum)

n=[0,0,0,0,0,0]
for k in range(600):
    from random import randint
    number=randint(1,6)
    for a in range(1,7):
        if a==number:
            n[a-1]+=1
for i in range(6):
    print('주사위가 %d인 경우는 %d번이다'%(i+1,n[i]))'''








