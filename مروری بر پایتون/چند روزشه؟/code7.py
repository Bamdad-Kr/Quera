from datetime import datetime

def day_calculator(date):
    date = datetime.strptime(date, '%Y-%m-%d')
    date2 = datetime.strptime("1999-01-14", '%Y-%m-%d')
    if (date - date2).days < 0:
        return 'Not yet born'
    else:
        return (date - date2).days
