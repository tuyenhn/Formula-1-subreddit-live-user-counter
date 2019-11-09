import os
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker


def plot(file_name):
    cwd = os.getcwd()
    x = []
    y = []
    try:
        file_dir = cwd + '\\' + file_name
    except:
        raise TypeError('arg must be of type string')
    with open(file_dir) as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip('\n')
            line = line.split(',')
            x.append(dt.datetime.strptime(line[0], '%c'))
            y.append(int(line[1]))

    fig, ax = plt.subplots()
    ax.plot(x, y)

    ax.yaxis.set_major_locator(ticker.AutoLocator())
    ax.yaxis.set_minor_locator(ticker.AutoMinorLocator())

    ax.xaxis.set_major_locator(ticker.AutoLocator())
    ax.xaxis.set_minor_locator(ticker.AutoMinorLocator())

    max_loc = y.index(max(y))
    ax.annotate('peak', (mdates.date2num(x[max_loc]), y[max_loc]), xytext=(
        -30, 40), textcoords='offset points', arrowprops=dict(arrowstyle='->'))
    min_loc = y.index(min(y))
    ax.annotate('bottom', (mdates.date2num(x[min_loc]), y[min_loc]), xytext=(
        -30, -40), textcoords='offset points', arrowprops=dict(arrowstyle='->'))

    ax.grid()
    fig.autofmt_xdate()
    plt.show()


plot('raw_data.txt')
