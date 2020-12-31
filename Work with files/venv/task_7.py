import json

with open("firms.txt", "r", encoding="UTF-8") as info:
    firms = info.read().split("\n")
    prof_list=[]
    for_average = []
    firm_base = []

    for line in firms:
        el = line.split( )
        firm = el[0]
        proceed = el[2]
        costs = el[3]

        firm_base.append(firm)

        profit = int(proceed) - int(costs)
        prof_list.append(profit)

        if profit >= 0:
            for_average.append(profit)

    data_firm = dict(zip(firm_base, prof_list))

    average = sum(for_average) / len(for_average)
    average_dict = {"average_profit" : average}

    info_firms = [data_firm, average_dict]
    print(info_firms)


with open("firms.json", "w") as write_f:
    json.dump(info_firms, write_f)
