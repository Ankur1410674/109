import random
import typing as counter
import plotly.express as px
import plotly.figure_factory as ff
import statistics as st

result=[]
count=[]
for i in range(0,1000):    
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    result.append(dice1+dice2)
    count.append(i)
fig = ff.create_distplot([result],["count"],show_hist=False)
#fig.show()
mean = st.mean(result)
print(mean)
median = st.median(result)
print(median)
mode = st.mode(result)
print(mode)
sd = st.stdev(result)
print(sd)
sd1start,sd1end = mean - sd , mean + sd
sd2start,sd2end = mean - (2*sd),mean + (2*sd)
sd3start,sd3end = mean - (3*sd) , mean + (3*sd)
listsd1 = [res for res in result if res>sd1start and res<sd1end]
listsd2 = [res for res in result if res>sd2start and res<sd2end]
listsd3 = [res for res in result if res>sd3start and res<sd3end]
print("{}%    of data lies with in 1 standard deviation".format(len(listsd1)*100.0/len(result)))
print("{}% of data lies with in 1 standard deviation".format(len(listsd2)*100.0/len(result)))
print("{}% of data lies with in 1 standard deviation".format(len(listsd3)*100.0/len(result)))