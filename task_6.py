def only_num(subject, end):
    if subject.endswith(end):
        subject = subject[:2]
    return subject

with open("lectures.txt", "r", encoding="UTF-8") as school:
    lectures = school.read().split("\n")
    subject = []
    hours_sum = []

    for line in lectures:
        sym = line.split( )
        lesson = sym[0]
        lecture = sym[1]
        practice = sym[2]
        lab = sym[3]

        subject.append(lesson)

        lec_num = only_num(lecture, "(лек)")
        pr_num = only_num(practice, "(пр)")
        lab_num = only_num(lab, "(лаб)")

        if lec_num == "-" and pr_num == "-":
            lec_num, pr_num = 0, 0
        elif lec_num == "-" and lab_num == "-":
            lec_num, lab_num = 0, 0
        elif pr_num == "-" and lab_num == "-":
            pr_num, lab_num = 0, 0
        elif lec_num == "-":
            lec_num = 0
        elif pr_num == "-":
            pr_num = 0
        elif lab_num == "-":
            lab_num = 0

        hours = int(lec_num) + int(pr_num) + int(lab_num)
        hours_sum.append(hours)

        hours_num = dict(zip(subject, hours_sum))

    print(hours_num)
