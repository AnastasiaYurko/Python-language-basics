from sys import argv

script_name, hours, rate, award = argv

def salary(hours_rate_award_list):
    sal = int(hours_rate_award_list[1]) * int(hours_rate_award_list[2]) + int(hours_rate_award_list[3])
    return sal

print(salary(argv))
