import pywhatkit as pyw

hrs = input("Enter hours in 24 hours format: ")
mins = input("Enter mins in 24 hours format: ")
phone_number = input("Enter the phone number with country code: ")
msg = input("Type the message you want to send--- \n")

pyw.sendwhatmsg(phone_no=phone_number, message=msg,
                time_hour=int(hrs), time_min=int(mins))
