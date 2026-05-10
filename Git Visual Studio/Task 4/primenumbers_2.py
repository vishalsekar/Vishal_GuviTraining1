#Given a Python List [10, 501, 22, 37, 100, 999, 87, 351], count all the prime numbers and create a new Python list containing those prime numbers.
l= [10, 501, 22, 37, 100, 999, 87, 351]

prime=[]
for i in l:
    p=0
    if p % i==1:
        print(i)
        p=p+1
        prime.append(i)



    # for j in i:
    #     if i%j==0:
    #         c=c+1
    #     if c==1
    #     print
