import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# creating function to import dataset 
def importing_datase(data='dataname_with_path'):
    df=pd.read_csv(data)
    return df


# creating a function for ploting bar chart
def plot_bar_chart(data,variable):
    c= data.select_dtypes(exclude=['object'])
    for i in c:
        plt.bar(height=data[i],x=data[variable])
        plt.ylabel('{}'.format(i))
        plt.xlabel(variable)
        plt.title('{} distribution'  .format(i))
        plt.show()



data=importing_datase(r'G:\Tutors club internship\Tutors-club-internship\imaginary_data.csv')
plot_bar_chart(data,'faculty_gender')

