per_cent = {'ТКБ' : 5.6, 'СКБ' : 5.9, 'ВТБ' : 4.28, 'СБЕР' : 4.0}
print("Предложения банков: ", per_cent)
money = int(input('Money: '))
deposite_sum = [int(i * money/100) for i in per_cent.values()]
print("Суммы депозитов:", deposite_sum)
print("Максимальная сумма депозита:", max(deposite_sum))