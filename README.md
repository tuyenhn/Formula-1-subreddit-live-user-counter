# Formula-1-subreddit-live-user-counter
A small project of mine

### Description:
Creating plots of reddit's Formula 1 subreddit user count every race weekend

### The workflow:
 - On Thursday, I will put logger.py up in an AWS EC2 server, which will log the subreddit's user count through reddit's API every 15 seconds
 - After the Sunday race, I will download raw_data.txt through FileZilla and split it into 3 different text files: 1.txt(Friday), 2.txt(Saturday) and 3.txt(Sunday)
 - Then I will use multiplotter.py with matplotlib and draw up the plot
 
P.S. I wrote the script from a long time ago but this was my first time putting it on GitHub. I planned to write a new one from scratch starting next season
