'''
Найдите сумму цифр трехзначного числа.
*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |



n = int(input('Введите трехзначное число'))
m = 0

while n:
    m = m + n % 10
    n = n // 10



print(m)
'''

n = 432
summa = 0
while n > 0:
    x = n % 10
    summa += x
    n //= 10
print(summa)    