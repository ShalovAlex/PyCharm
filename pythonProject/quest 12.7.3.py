money = int(input("Enter the amount you are investing:"))

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

procent = list(per_cent.values())
bank_TKB = round(procent[0] / 100 * money)
bank_CKB = round(procent[1] / 100 * money)
bank_VTB = round(procent[2] / 100 * money)
bank_SBER = round(procent[3] / 100 * money)

deposit = [bank_TKB, bank_CKB, bank_VTB, bank_SBER]
print("Possible income:", deposit)

deposit.sort()
print("The maximum, amount you can earn - ", deposit[-1])
