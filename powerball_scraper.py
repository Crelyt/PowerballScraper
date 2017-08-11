import requests

powerball_url = 'http://www.powerball.com/powerball/winnums-text.txt'
response = requests.get(powerball_url)
response = response.text
number_list = response.split('\r\n')
weekly_list = []

for week in number_list[1:]:
    week_date = week[:10]
    wb1 = week[12:14]
    wb2 = week[16:18]
    wb3 = week[20:22]
    wb4 = week[24:26]
    wb5 = week[28:30]
    pb = week[32:34]
    pp = week[36:]
    week_dict = {'date': week_date,
                 'WB1': wb1,
                 'WB2': wb2,
                 'WB3': wb3,
                 'WB4': wb4,
                 'WB5': wb5,
                 'PB': pb,
                 'PP': pp}

    weekly_list.append(week_dict)

this_weeks_numbers = weekly_list[0]

print(this_weeks_numbers['date'])
print(this_weeks_numbers['WB1'])

