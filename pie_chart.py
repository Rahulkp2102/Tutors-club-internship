import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# creating function to import dataset 
def importing_datase(data='dataname_with_path'):
    df=pd.read_csv(data)
    return df

# creating a function for ploting pie chart
def plot_pie_chart(data):
    c= data
    for i in c:
        plt.pie(data[i].value_counts().head(7), labels=data[i].value_counts().head(7).index,shadow=True,autopct='%1.1f%%')
        plt.title('{} pie plot '.format(i))
        plt.show()


# Ploting pie chart
df=importing_datase(r'G:\Tutors club internship\Tutors-club-internship\imaginary_data.csv')
plot_pie_chart(df)