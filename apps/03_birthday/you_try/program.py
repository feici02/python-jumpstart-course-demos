import datetime

title_len = 40

print('-' * title_len)
print('BIRTHDAY APP'.center(title_len))
print('-' * title_len)
print()

def get_bday():
    year = int(input('What year were you born [YYYY]? '))
    month = int(input('What month were you born [MM]? '))
    day = int(input('What day were you born [DD]? '))

    print('It looks like you were born on {}/{}/{}'.format(month, day, year))
    bday = datetime.datetime(year, month, day)
    return bday

def get_day_diff(tday, bday):
    bday_in_this_year = datetime.datetime(tday.year, bday.month, bday.day)
    day_diff = tday - bday_in_this_year
    return day_diff.days

def print_msg(day_diff):
    if day_diff < 0:
        print('Your birthday will be in {} days.'.format(-day_diff))
    elif day_diff > 0:
        print('Your birthday has passed {} days'.format(day_diff))
    else:
        print('Today is your birthday.')

if __name__ == '__main__':
    bday = get_bday()
    tday = datetime.datetime.now()
    day_diff = get_day_diff(tday, bday)
    print_msg(day_diff)