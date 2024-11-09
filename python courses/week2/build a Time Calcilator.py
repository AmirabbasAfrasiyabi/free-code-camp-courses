def add_time(start, duration, day_of_week=None):
    # Parse the start time
    time, period = start.split()
    start_hour, start_minute = map(int, time.split(':'))
    
    # Convert PM to 24-hour format
    if period == "PM" and start_hour != 12:
        start_hour += 12
    elif period == "AM" and start_hour == 12:
        start_hour = 0
    
    # Parse the duration
    dur_hour, dur_minute = map(int, duration.split(':'))
    
    # Calculate the new time
    total_minutes = start_minute + dur_minute
    extra_hours = total_minutes // 60
    new_minute = total_minutes % 60

    total_hours = start_hour + dur_hour + extra_hours
    new_hour = total_hours % 24
    days_later = total_hours // 24

    # Convert back to 12-hour format
    new_period = "AM" if new_hour < 12 else "PM"
    if new_hour == 0:
        new_hour = 12
    elif new_hour > 12:
        new_hour -= 12

    # Calculate the day of the week if provided
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if day_of_week:
        day_index = days_of_week.index(day_of_week.capitalize())
        new_day_index = (day_index + days_later) % 7
        new_day = days_of_week[new_day_index]
    
    # Format the result time
    new_time = f"{new_hour}:{new_minute:02d} {new_period}"
    
    if day_of_week:
        new_time += f", {new_day}"
    
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time

# Examples
print(add_time('3:00 PM', '3:10'))  # Returns: 6:10 PM
print(add_time('11:30 AM', '2:32', 'Monday'))  # Returns: 2:02 PM, Monday
print(add_time('11:43 PM', '24:20', 'Tuesday'))  # Returns: 12:03 AM, Thursday (2 days later)
print(add_time('6:30 PM', '205:12'))  # Returns: 7:42 AM (9 days later)
