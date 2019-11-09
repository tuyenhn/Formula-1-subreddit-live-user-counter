from datetime import datetime, timedelta

with open('sample.txt', 'r+') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip('\n')
        line = line.split(',')
        datetime_obj = datetime.strptime(line[0], '%c')
        datetime_obj += timedelta(hours=1)

        f.write(datetime_obj.strftime('%c') + f',{line[1]}\n')
        print(datetime_obj)
