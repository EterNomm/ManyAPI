# Reference :
#	https://stackoverflow.com/a/58004773


def convert(duration, mode="s"):
   day_time = duration.split('T')
   day_duration = day_time[0].replace('P', '')
   day_list = day_duration.split('D')
   if len(day_list) == 2:
      day = int(day_list[0])
      day_list = day_list[1]
   else:
      day = 0
      day_list = day_list[0]
   hour_list = day_time[1].split('H')
   if len(hour_list) == 2:
      hour = int(hour_list[0])
      hour_list = hour_list[1]
   else:
      hour = 0
      hour_list = hour_list[0]
   minute_list = hour_list.split('M')
   if len(minute_list) == 2:
      minute = int(minute_list[0])
      minute_list = minute_list[1]
   else:
      minute = 0
      minute_list = minute_list[0]
   second_list = minute_list.split('S')
   if len(second_list) == 2:
      second = int(second_list[0])
   else:
      second = 0
   
   if mode == "s":
   	return f"{day} Days : {hour} Hour : {minute} Minute : {second} Second"
   else:
   	return f"{day}:{hour}:{minute}:{second}"
