hourspernight = input("How many hours per night do you sleep? :")
#int changes the variable into an integer value.
hoursperweek = int(hourspernight) * 7
print ("You sleep:",hoursperweek,"hours per week.")
#float allows the integer value to have decimal points.
hourspermonth = float(hoursperweek) * 4.45
print ("and:",hourspermonth,"hours per month.")
dayspermonth = float(hourspermonth) / 24
# * multiplies and / divides
print ("this is equivelant to sleeping",dayspermonth,"days per month")