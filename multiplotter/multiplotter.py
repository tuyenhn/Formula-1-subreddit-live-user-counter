import os
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.dates as mdates

count = []
time = []
cwd = os.getcwd()
data_dir = os.listdir()
for file in data_dir:
    if file.endswith('.txt'):
        file_dir = cwd + '\\' + file

        x = []
        y = []
        with open(file_dir) as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip('\n')
                line = line.split(',')
                x.append(dt.datetime.strptime(line[0], '%c'))
                y.append(int(line[1]))

        time.append(x)
        count.append(y)
        x = None
        y = None

time_li = []
count_li = []
fig = plt.figure(figsize=(17, 8.5))
subplots = [plt.subplot(221, title='Friday'),
            plt.subplot(222, title='Saturday'),
            plt.subplot(212, title='Sunday')]

for subplot, i in zip(subplots, range(0, len(subplots))):
    xnew = time[i]
    ynew = count[i]
    subplot.plot(xnew, ynew)

    time_li.append(xnew)
    count_li.append(ynew)

    subplot.yaxis.set_major_locator(ticker.AutoLocator())
    subplot.yaxis.set_minor_locator(ticker.AutoMinorLocator())

    subplot.xaxis.set_major_locator(ticker.AutoLocator())
    subplot.xaxis.set_minor_locator(ticker.AutoMinorLocator())


FP1_starts = [time_li[0][2612], count_li[0][2612]]
FP2_starts = [time_li[0][3561], count_li[0][3561]]

FP3_starts = [time_li[1][3087], count_li[1][3087]]
Q_starts = [time_li[1][3799], count_li[1][3799]]

Race_starts = [time_li[2][3127], count_li[2][3127]]

print(FP1_starts, FP2_starts, FP3_starts, Q_starts, Race_starts, sep='\n')

subplots[0].annotate('FP1 starts', (mdates.date2num(FP1_starts[0]), FP1_starts[1]), xytext=(
    -60, 40), textcoords='offset points', arrowprops=dict(arrowstyle='->'))
subplots[0].annotate('FP2 starts', (mdates.date2num(FP2_starts[0]), FP2_starts[1]), xytext=(
    -30, 40), textcoords='offset points', arrowprops=dict(arrowstyle='->'))

subplots[1].annotate('FP3 starts', (mdates.date2num(FP3_starts[0]), FP3_starts[1]), xytext=(
    -20, -40), textcoords='offset points', arrowprops=dict(arrowstyle='->'))
subplots[1].annotate('Qualifying starts', (mdates.date2num(Q_starts[0]), Q_starts[1]), xytext=(
    -90, 40), textcoords='offset points', arrowprops=dict(arrowstyle='->'))

subplots[2].annotate('Race starts', (mdates.date2num(Race_starts[0]), Race_starts[1]), xytext=(
    -10, -30), textcoords='offset points', arrowprops=dict(arrowstyle='->'))


fig.suptitle('r/F1 active user count on race weekend', fontsize=20)
fig.autofmt_xdate()
plt.show()
