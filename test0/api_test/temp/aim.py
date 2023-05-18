s=input()
n,aim=int(s.split(' ')[0]),int(s.split(' ')[1])
charge_list=[int(i) for i in input().split(' ')]
charge_list.sort(reverse=True)
result=0
for charge in charge_list:
    result+=int(aim/charge)
    aim=aim%charge
print(result)
