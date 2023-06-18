from squares import func
#a = []
#a = set()
#a = [{"Name": "Oleg","Surname": "Udod"},{"Name": "Viktor","Surname": "Dolmatov"}];
#print(a[0]["Name"]+" "+a[1]["Surname"]);
for i in range (1,20):
    print(str(i) + "^2= " + str(func(i,2)));

for i in range (1,20):
    print(str(i) + "^3= " + str(func(i,3)));
