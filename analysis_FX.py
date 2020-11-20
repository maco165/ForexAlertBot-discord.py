import csv
import locale
import datetime

def transtime(Day_of):
    year = int(Day_of.split('.')[0])
    month = int(Day_of.split('.')[1])
    Days = int(Day_of.split('.')[2])
    dt = datetime.datetime(year, month, Days)
    return dt

csv_file = open("TickerCSV\\GBPJPY\\H4\\H4_ALL.csv", "r", encoding="utf_8", newline="" )
f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
i = 1993
for row in f:
    if str(i) in row[0]:
        ratio = (float(row[2])-float(row[5]))
        difference = (float(row[3])-float(row[4]))
        month = int(row[0].split('.')[1])
        Days = int(row[0].split('.')[2])
        if ratio > 0:
            line = 1
        else:
            line = 0
        with open('Result\\GBPJPY\\H4\\'+str(i)+'.csv', mode='a',newline="") as f:
            writer = csv.writer(f)
            writer.writerow([month,Days,transtime(row[0]).strftime('%a'),line,round(ratio,2),round(difference,2),row[6]])
        
        print(row[0]+' 出力')
        i=int(i)
    else:
        i+=1