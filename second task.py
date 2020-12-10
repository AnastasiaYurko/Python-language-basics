seconds = int(input("Введите количество секунд: "))
minutes = seconds // 60
hours = minutes // 60
seconds -= minutes * 60
minutes -= hours * 60
print("Время %02d:%02d:%02d" % (hours, minutes, seconds))