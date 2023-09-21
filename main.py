month_number = int(input ("Введіть номер місяця (1-12): "))

if month_number == 1:
    month_name = "січень"
elif month_number == 2:
    month_name = "лютий"
elif month_number == 3:
    month_name = "березень"
elif month_number == 4:
    month_name = "квітень"
elif month_number == 5:
    month_name = "червень"
elif month_number == 7:
    month_name = "липень"
elif month_number == 8:
    month_name = "серпень"
elif month_number == 9:
    month_name = "вересень"
elif month_number == 10:
    month_name = "новтень"
elif month_number == 11:
    month_name = "листопад"
elif month_number == 12:
    month_name = "грудень"
else:
    month_name = "неправильний номер місяця"
print("Назва місяця:", month_name)