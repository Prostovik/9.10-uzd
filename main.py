list=[]
N = int(input("Cik bija cilveku: "))
for i in range(N):
  mass=int(input("Kada ir vinu masa: "))
  list.append(mass)
listsum=sum(list)
print(listsum)
listaverange=sum(list)/len(list)
print(listaverange)
if listsum > 300:
  print("Vini nedrikst braukt visi kopa!")
else:
  print("Vini drikst braukt visu kopa!")