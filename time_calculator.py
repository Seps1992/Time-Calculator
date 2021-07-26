def add_time(start, duration, day=None):
  
    day_map = {
        "Saturday": 0,
        "Sunday": 1,
        "Monday": 2,
        "Tuesday": 3,
        "Wednesday": 4,
        "Thursday": 5,
        "Friday": 6
    }
    
    time, miday = start.split()
    hour, minutes = time.split(':')
    hour = int(hour)
    minutes = int(minutes)

    
    if miday == "PM":
        hour += 12

    
    duration_hour, duration_minutes = duration.split(':')
    duration_hour = int(duration_hour)
    duration_minutes = int(duration_minutes)

    
    total_minutes = minutes + duration_minutes
    real_minutes = total_minutes % 60
    extra_hours = total_minutes // 60
    total_hour = hour + duration_hour + extra_hours

    
    real_hour = (total_hour % 24) % 12

    
    if real_hour == 0:
        real_hour = 12
    real_hour = str(real_hour)

    
    total_day = (total_hour // 24)

    
    real_time = ""
    if (total_hour % 24) <= 11:
        real_time = "AM"
    else:
        real_time = "PM"

    
    if real_minutes <= 9:
        real_minutes = '0' + str(real_minutes)
    else:
        real_minutes = str(real_minutes)
    
    time_stamp = real_hour + ":" + real_minutes + ' ' + real_time
    if day == None:
        if total_day == 0:
            return time_stamp
        if total_day == 1:
            return time_stamp + ' (next day)'
        return time_stamp + ' (' + str(total_day) + ' days later)'
    else:
        ans_day = (day_map[day.lower().capitalize()] + total_day) % 7
        for i, j in day_map.items():
            if j == ans_day:
                ans_day = i
                break
        if total_day == 0:
            return time_stamp + ', ' + ans_day
        if total_day == 1:
            return time_stamp + ', ' + ans_day + ' (next day)'
        return time_stamp + ', ' + ans_day + ' (' + str(
            total_day) + ' days later)'