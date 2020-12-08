days = ["monday","Tuesday","Wednesday","sunday"]

for day in days:
    if days.index(day) == len(days)-1:
        print("Toi khong di lam " +day)
    else:
        print("toi di lam "+day)