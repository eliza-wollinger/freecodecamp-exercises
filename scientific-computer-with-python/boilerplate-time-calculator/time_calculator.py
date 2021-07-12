def add_time(start, duration, start_day=""):

    if duration == "0:00":
        return f"{start}{', ' + start_day if start_day != '' else ''}"
    else:
        
        days = {0:"Monday", 1:"Tuesday", 2:"Wednesday", 3: "Thursday", 4:"Friday", 5:"Saturday", 6:"Sunday"}
        
        period_changer = {"AM" : "PM", "PM" :"AM"}

        start_hour = int(start[:-6])
        start_minute = int(start[-5:-3])
        period = start[-2:]

        duration_hours = int(duration[:-3])
        duration_minutes = int(duration[-2:])

        new_hour = start_hour + duration_hours
        new_minute = start_minute + duration_minutes
        
        if new_minute < 60:
            new_minute = new_minute 
        else:
            new_minute -= 60
            new_hour += 1

        if new_hour < 12:
            new_hour = new_hour
            new_period = period
            return f"{new_hour}:{new_minute if len(str(new_minute)) > 1 else '0'+str(new_minute)} {new_period}{', ' + start_day if start_day != '' else ''}"
        elif new_hour == 12:
            p = 0
            new_period = period_changer[period]
            p += 1
        else:
            p = 0
            while new_hour > 12:
                new_hour -= 12
                p += 1
                if new_hour == 12:
                    p +=1 
                    break

        if p % 2 == 0:
            new_period = period 
        else:
            new_period = period_changer[period] 

        if p > 1:
            n_days = round(p / 2) if int(p/2)%2 != 0 else round(p/2) + 1
        else:
            n_days = 1 if new_period == "AM" else 0
        
        if n_days == 0:
            return f"{new_hour}:{new_minute if len(str(new_minute)) > 1 else '0'+str(new_minute)} {new_period}{', ' + start_day if start_day != '' else ''}"
        elif start_day != '':
            print(n_days)
            days_values = list(days.values())
            start_day_key = days_values.index(start_day.casefold().title())
            new_day = days[n_days - (7 * int(n_days / 7)) + start_day_key] if (n_days + start_day_key)%7 != 0 else days[0]
            return f"{new_hour}:{new_minute if len(str(new_minute)) > 1 else '0'+str(new_minute)} {new_period}{', ' + new_day if start_day != '' else ''} ({str(n_days) + ' days later' if n_days > 1 else 'next day'})"
        else:
            return f"{new_hour}:{new_minute if len(str(new_minute)) > 1 else '0'+str(new_minute)} {new_period}{', ' + new_day if start_day != '' else ''} ({str(n_days) + ' days later' if n_days > 1 else 'next day'})"