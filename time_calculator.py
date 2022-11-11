
def get_days_later(days):
    dl = ''
    if days == 1:
        dl = '(next day)'

    elif days > 1:
        dl += f'({days} days later)'
    
    return dl

def add_time(start, duration, day = False):
    week_days = [
        'monday', 'tuesday',
        'wednesday', 'thursday',
        'friday', 'saturday',
        'sunday']
    
    # set variables
    days_later = 0  #to calculate days later string later in the function 
    half_day = 12 #hours
    one_day = 24 
     
    # split variables
    hours, mins = start.split(':')
    mins, period = mins.split(' ')
    dh, dm = duration.split(':')
    
    #clean data: string into int
    hours = int(hours)
    mins = int(mins)
    dh = int(dh)
    dm = int(dm)
    
    #lower string for ease 
    period = period.strip().lower()
    
    #calculate the total hour
    total_hours = hours + dh
    total_mins = mins + dm

    
    #calcuate mins and totals based on min 
    if total_mins > 60: 
        total_hours += 1
        total_mins = int(total_mins%60)
    
    if dh or dm:
        #add 1 more to pm 
        if period == 'pm' and total_hours >= 12:
            days_later +=1
        
        if total_hours >= one_day:
            days_later = int(total_hours/24)

    tth = total_hours
    print(int(total_hours/24))
    print(days_later)

    while True:
        if tth < 12:
            break
        elif tth >= 12:
            if period == 'am':
                period ='pm'
            elif period == 'pm':
                period = 'am'
            tth -= 12

    remaining_hours = int(total_hours%12) or hours+1
    remaining_mins = total_mins
            
    results = f'{remaining_hours}:{remaining_mins:02} {period.upper()}'

    
    if day:
        day = day.strip().lower()
        selected_day = int((week_days.index(day)+days_later)%7)
        current_day = week_days[selected_day]
        
        results += f', {current_day.title()} {get_days_later(days_later)}' 
    else:
        results += f' {get_days_later(days_later)}'
        
    return results.strip() 
    
    
print(add_time("6:30 PM", "205:12", 'fRIDAY'))

print(add_time("11:43 PM", "24:20"))

print(add_time("11:43 AM", "00:20"))

print(add_time("3:00 PM", "3:10"))

print(add_time("11:30 AM", "2:32", "Monday"))

print(add_time("2:59 AM", "00:00"))
