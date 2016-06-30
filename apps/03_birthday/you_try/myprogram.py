from datetime import date


def print_header():
    print('-'*40)
    print(' '*10 + 'BIRTHDAY APP')
    print('-'*40)


def get_birthday():
    year = int(input("What year were you born [YYYY]? "))
    month = int(input("What month were you born [MM]? "))
    day = int(input("What day were you born [DD]? "))
    return date(year, month, day)


def compute_days_between_dates(date1, date2):
    d1 = date1
    d2 = date(d1.year, date2.month, date2.day)
    return (d1-d2).days


def output_bday_info(days):
    if days < 0:
        print('Your birthday has passed ' + str(abs(days)) + ' days.')
    elif days > 0:
        print('Your birthday is in ' + str(days) + ' days.')
    else:
        print('Today is your birthday.')


def main():
    print_header()
    bday = get_birthday()
    tday = date.today()
    days = compute_days_between_dates(bday, tday)
    output_bday_info(days)


main()