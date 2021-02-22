from datetime import date, datetime

bd= input("please enter your birthday(dd.mm.yyyy): ")
bday= bd[:2]
bmonth = bd[3:5]
byear= bd[6:]
bdate = date(int(byear),int(bmonth),int(bday))
todaytime= datetime.now()

agey = todaytime.year-bdate.year
agem = todaytime.month-bdate.month
aged= todaytime.day- bdate.day
if agem < 0 or aged <0 :
    agey -=1
    aged = 30 + aged
    if agem <0:
        agem= 12 + agem
print("You are: " + str(todaytime.minute) + " minutes, " + str(todaytime.hour)
      + " hours, " + str(aged) + " days, " + str(agem) + " months, " + str(agey) + " years old.")



