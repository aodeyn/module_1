points = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
list_students = list(students)
list_students = sorted(list_students)
n = 0
m = len(points)
while n < m:
   print(list_students[n], sum(points[n])/len(points[n]))
   n = n+1
