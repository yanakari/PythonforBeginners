a, b, c=map(int, input().split())
d=b**2-4*a*c
if a==0:
    print("Мы такое не решаем")
else:
    print("Это квадратное уравнение")
    if d<0:
        print("Решений нет")
    elif d==0:
        x=-b/(2*a)
        print(x)
    elif d>0:
        x1=(-b-d**0.5)/(2*a)
        x2 = (-b + d ** 0.5) / (2 * a)
        print(x1, x2)