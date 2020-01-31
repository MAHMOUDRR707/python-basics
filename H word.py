thickness=5

for i in range(0,thickness):
    print((('H'*(i))+('H'*(i+1))).center((thickness*2)-1))

for i in range(0,thickness+1):
    print(('H'*(thickness)).center((thickness)+4)+(('H'*(thickness)).rjust(((thickness)*3)+3)))

for i in range(0,thickness):
    print((('H'*(thickness)*(thickness)).rjust(((thickness)*5)+2)))

for i in range(0,thickness+1):
    print(('H'*(thickness)).center((thickness)+4)+(('H'*(thickness)).rjust(((thickness)*3)+3)))


for i in range(thickness-1,-1,-1):
    print((('H'*(i))+('H'*(i+1))).center((thickness*10)-1))   
