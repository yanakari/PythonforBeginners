r=int(input())
x, y = map(int, input().split())
#Расстояние от начала координат до искомой точки
z=(x**2+y**2)**0.5
if r>=z:
    print("Лежит")
else:
    print("не лежит")