import sys
#Basic classes
# class Point:
#     def set_coord(self,x,y):
#         self.x=x
#         self.y=y
#     def sum(self):
#         return self.x+self.y
# p=Point();
# try:  
#     p.set_coord(int(input('Enter x: ')),int(input('Enter y: ')))
# except ValueError:
#     print('X and Y must have int value!')
#     sys.exit(1)
# print(p.__dict__,"==",p.sum())

class Point():
    def __init__(self,x,y):
        print(f'Creating {self}!')
        self.x=x
        self.y=y
    def __del__(self):
        print(f'Deleting {self}!')
    def sum(self):
        return self.x+self.y

p=Point(12,32)
p1 = Point(11,24)
print(p.sum())