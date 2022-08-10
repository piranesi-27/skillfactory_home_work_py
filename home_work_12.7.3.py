money = int(input('Введите сумму: ')) #запрашиваем сумму

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0} #словарь с названием банков и процентной ставкой

values = list(per_cent.values()) #выделяем из словаря процентные ставки и заносим в список

deposit = [int(money / 100 * values[0]), int(money / 100 * values[1]), int(money / 100 * values[2]), int(money / 100 * values[3])] #рассчитываем депозит-
#обращаясь к индексу ставки из списка, отбрасываем дробную часть и оборачиваем в список

deposit_max = [int(max(deposit))] #определяем максимальную сумму

print('deposit = ' + str(deposit)) #выводим все значения

print('Максимальная сумма, которую вы можете заработать — ' + 'deposit' + str(deposit_max)) #выводим максимальную сумму