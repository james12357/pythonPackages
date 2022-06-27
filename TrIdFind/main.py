import csv
txt = open("id.csv", "r", encoding="utf-8-sig")
dic = {}
with txt:
    rd = csv.reader(txt)
    for i in rd:
        dic[i[0]] = i[1]
while True:
    dig = input("READY>")
    if dig.startswith("##"):
        dig = dig[2:]
        for i, j in dic.items():
            if j == dig:
                print(f"{j}:{i}")
    else:
        for i in dic:
            if dig in i:
                print(f"{i}:{dic[i]}")


