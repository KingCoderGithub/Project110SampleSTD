import pandas as pd
import plotly.figure_factory as ff
import csv
import statistics as st
import plotly.graph_objects as go
import random

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].to_list()

populationSd = st.stdev(data)

def showFig(meanList) :
    df = meanList
    mean = st.mean(df)
    fig = ff.create_distplot([df], ["Reading Time"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="mean"))
    fig.show()
populationMean = st.mean(data)

def randomSetOfMean(counter) :
    dataSet = []
    for i in range(0, counter):
        randomIndex = random.randint(0, len(data) - 1)
        value = data[randomIndex]
        dataSet.append(value)
    mean = st.mean(dataSet)
    return mean

# Sample for thousand data sets
def setup() :
    meanList = []
    for i in range(0, 1000):
        setOfMeans = randomSetOfMean(100)
        meanList.append(setOfMeans)
    showFig(meanList)
    mean = st.mean(meanList)
    print("Mean of Samples: ", mean)

setup()

def std() :
    meanList = []
    for i in range(0, 1000):
        setOfMeans = randomSetOfMean(100)
        meanList.append(setOfMeans)
    showFig(meanList)
    std = st.stdev(meanList)
    print("Standard Deviation of Samples: ", std)

std()
    

print("Popuation Mean : " , populationMean)
print("Poulation Standard Deviation : ", populationSd)