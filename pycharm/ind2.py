s = input().lower()
s1 = s.replace('жы','жи')
s1 = s1.replace('шы','ши')
if s1 == s:
    print('Ok')
else:
    print('Есть ошибки')
