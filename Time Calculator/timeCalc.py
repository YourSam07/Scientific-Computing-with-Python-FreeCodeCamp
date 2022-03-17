def add_time(start, duration, weekDay=""):
    week_days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

    time, am_pm = start.split()
    hrs, mins = time.split(':')
    dur_hrs, dur_mins = duration.split(':')

    half_day = 12
    full_day = 24
    no_of_days = 0
    wi = 0 if len(weekDay) == 0 else week_days.index(weekDay.lower())

    add_hrs = int(hrs) + int(dur_hrs)
    add_mins = int(mins) + int(dur_mins)

    if add_mins >= 60:
        add_hrs += add_mins // 60
        add_mins = add_mins % 60

    no_of_days += add_hrs//24
    if am_pm == "PM" and add_hrs > half_day:
        no_of_days += 1
        wi += no_of_days
        if wi > 6:
            wi = wi - 7 * (wi // 7)
    if am_pm == "AM" and add_hrs > full_day:
        wi += no_of_days
        if wi > 6:
            wi = wi - 7 * (wi // 7)

    am_pm_flip = {"AM": "PM", "PM": "AM"}
    no_of_flips = add_hrs / 12
    am_pm = am_pm_flip[am_pm] if int(no_of_flips) % 2 == 1 else am_pm

    new_hrs = str(add_hrs % 24 - 12) if add_hrs % 24 > 12 else str(add_hrs % 24)
    new_min = "0" + str(add_mins % 60) if add_mins % 60 < 10 else str(add_mins % 60)
    new_time = ''
    if len(weekDay) >= 6:
        if no_of_days == 0:
            new_time = ":".join((new_hrs, new_min)) + " " + am_pm + ", " + week_days[wi].title()
        if no_of_days == 1:
            new_time = ":".join((new_hrs, new_min)) + " " + am_pm + ", " + week_days[wi].title() + " (next day)"
        if no_of_days > 1:
            new_time = ":".join((new_hrs, new_min)) + " " + am_pm + ", " + week_days[wi].title() + " (" + str(
                no_of_days) + " days later)"
    else:
        if no_of_days == 0:
            new_time = ":".join((new_hrs, new_min)) + " " + am_pm
        if no_of_days == 1:
            new_time = ":".join((new_hrs, new_min)) + " " + am_pm + " (next day)"
        if no_of_days > 1:
            new_time = ":".join((new_hrs, new_min)) + " " + am_pm + " (" + str(no_of_days) + " days later)"

    return new_time

