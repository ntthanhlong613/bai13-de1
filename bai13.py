a,b,c=map(int,input().split())
if a+b>c and b+c>a and c+a>b:
    if a**2+c**2==b**2 or b**2+a**2==c**2 or c**2+b**2==a**2:
        print('tg vuong')
    elif a==b==c:
        print('tg deu')
    elif a==b or b==c or c==a:
        print('tg can')
    else:
        print('tg thuong')

    