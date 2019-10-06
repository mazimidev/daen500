hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
try:
    otHours = float(hours)%40
    otRate = float(rate)*1.5
    print (otHours)
    print (otRate)
except:
    print('please enter numeric')

else:
    if float(hours) > 40:
        regPay=40 * float(rate)
        print(regPay)
        otPay=otHours * otRate
        print('yay OT')
        print(otPay)
        totPay=regPay + otPay
        print(totPay)
    else:
        pay = (int(hours) * float(rate))
        print ('No OT')
        print (pay)
