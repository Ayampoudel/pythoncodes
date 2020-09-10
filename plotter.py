import numpy as np
import pandas as pd
import plotly as pl
import plotly.offline as po
import cufflinks as cf
from plotly.offline import init_notebook_mode, iplot
from plotly.graph_objs import *
po.init_notebook_mode(connected = True)
cf.go_offline()

#function to create dataframe based on the user choice
def Createdata(data):
    if data==1:
        x=np.random.rand(4,5)
        df=pd.DataFrame(x,columns=['A','B','C','D','E'])
    elif data==2:
        print("Input the values for  columns")
        i=0
        col=[0,0,0,0,0]
        for i in [0,1,2,3,4]:
            col[i]=input("col")
            i=i+1

        print("enter the values for 1st row")
        i=0
        r1=[0,0,0,0,0]
        for i in [0,1,2,3,4]:
            r1[i]=int(input())
            i=i+1

        print("enter the values for 2nd row")
        i=0
        r2=[0,0,0,0,0]
        for i in [0,1,2,3,4]:
            r2[i]=int(input())
            i=i+1

        print("enter the values for 3rd row")
        i=0
        r3=[0,0,0,0,0]
        for i in [0,1,2,3,4]:
            r3[i]=int(input())
            i=i+1

        print("enter the values for 4th row")
        i=0
        r4=[0,0,0,0,0]
        for i in [0,1,2,3,4]:
            r4[i]=int(input())
            i=i+1

        df=pd.DataFrame([r1,r2,r3,r4],columns=col)

    elif data==3:
        filename=input("Enter the file name")
        x=pd.read_csv(filename)
        df=pd.DataFrame(x)
    else:
        print ("dataset cannot be created")

    return df



#function to do the plotting if user wants to plot all the data
def plotter(plot):
    if plot==1:
        yourplot=df.iplot(kind="scatter")
    elif plot==2:
        yourplot=df.iplot(kind="scatter",mode="markers")
    elif plot==3:
        yourplot=df.iplot(kind="box")
    elif plot==4:
        yourplot=df.iplot(kind="bar")
    elif plot==5:
        youplot=df.iplot(kind="hist")
    elif plot==6:
        yourplot=df.iplot(kind="surface")
    else:
        yourplot=print("only select form 1 to 6")

    return yourplot



#function to do the plotting if the user wants to plot for selected columns
def plotter2(plot):
    col=int(input("Enter the number of columns you want to plot"))
    if col==1:
        colname=int(input("enter the column you want to plot"))
        if plot==1:
            yourplot=df[colname].iplot(kind='scatter')
        elif plot==2:
            yourplot=df[colname].iplot(kind='scatter',mode='markers')
        elif plot==3:
            yourplot=df[colname].iplot(kind='box')
        elif plot==4:
            yourplot=df[colname].iplot(kind='bar')
        elif plot==5:
            yourplot=df[colname].iplot(kind='hist')
        else:
            yourplot=print("surface plot and bubble plot need more the one columns")

    elif col==2:
        x=input("Enter the first column")
        y=input("Enter the second column")
        if plot==1:
            yourplot=df[[x,y]].iplot(kind="scatter")
        elif plot==2:
            yourplot=df[[x,y]].iplot(kind="scatter",mode="markers")
        elif plot==3:
            yourplot=df[[x,y]].iplot(kind="box")
        elif plot==4:
            yourplot=df[[x,y]].iplot(kind="bar")
        elif plot==5:
            yourplot=df[[x,y]].iplot(kind="hist")
        elif plot==6:
            yourplot=df[[x,y]].iplot(kind="surface")
        elif plot==7:
            size=input("Enter the size column for bubble plot")
            yourplot=df.iplot(kind="bubble",x=x,y=y,size=size)
        else:
            yourplot=print("SORRY BRO")



    elif col==3:
        x=input("Enter the first column")
        y=input("Enter the second column")
        z=input("Enter third column")
        if plot==1:
            yourplot=df[[x,y,z]].iplot(kind="scatter")
        elif plot==2:
            yourplot=df[[x,y,z]].iplot(kind="scatter",mode="markers")
        elif plot==3:
            yourplot=df[[x,y,z]].iplot(kind="box")
        elif plot==4:
            yourplot=df[[x,y,z]].iplot(kind="bar")
        elif plot==5:
            yourplot=df[[x,y,z]].iplot(kind="hist")
        elif plot==6:
            yourplot=df[[x,y,z]].iplot(kind="surface")
        elif plot==7:
            size=input("Enter the size column for bubble plot")
            yourplot=df.iplot(kind="bubble",x=x,y=y,z=z,size=size)
        else:
            yourplot=print("SORRY BRO")


    else:
        yourplot=print("SORRY BRO")


    return yourplot


#main function
def main(type):
    if type==1:
        print("Select the plot you want to use")
        print('1.Line plot')
        print('2.Scatter plot')
        print("3.Box plot")
        print("4.Bar Plot")
        print("5.Histogram")
        print("6.Surface plot")
        plot=int(input("enter your choice"))
        plotter(plot)
    elif type==2:
        print("Select the plot you want to use")
        print('1.Line plot')
        print('2.Scatter plot')
        print("3.Box plot")
        print("4.Bar Plot")
        print("5.Histogram")
        print("6.Surface plot")
        print("7.Bubble plot")
        plot=int(input("enter your choice"))
        plotter2(plot)
    else:
        print("You cannot plot otherwise")

#first ask the user the kind of data he/she wants to Input
print("What do you want?")
data=int(input("1.Random data \n 2.Customized Data(With 4 rows and 5 columns)\n3.Data from a file"))
df=Createdata(data)
print("The selected dataframe is")
print(df)

#Now to check weather the user wants to plot all the data or select data themselves
print("Do you want to plot for full data or selected columns(1 or 2)")
type=int(input("Enter your choice"))
main(type)
