import time
input_time = input("Please enter the date/time to be counted down as in the following format\n\
  DD/MM/YYYY HH:MM:SS : ")
countdown = time.strptime(input_time, "%d/%m/%Y %H:%M:%S")
countdown_t = time.mktime(countdown)

while time.mktime(time.localtime()) < countdown_t:
    time.sleep(1)
    c_time = time.strftime('%d/%m/%Y %H:%M:%S', time.localtime())
    print(f"\r{c_time}  {int(countdown_t - time.mktime(time.localtime()))} seconds left.", end='')
print(f"\nTime is UP!")



