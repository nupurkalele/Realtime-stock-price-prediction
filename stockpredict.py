import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from sklearn.linear_model import LinearRegression
from datetime import timedelta
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)



#GENERATING CHARTS FUNCTION
def gen_charts1(stock_name):
    
    #IMPORTING STOCK DATA
    stock_data = yf.Ticker(stock_name)
    stock_df1 = stock_data.history(period='1mo', interval='1d')
    
    current_price = stock_df1['Close'].iloc[-1]


    
    #FIRST CHART
    x1 = stock_df1.index.to_numpy()
    y1 = stock_df1['Close'].to_numpy()
    #Stock price line plot 
    fig, (ax1, ax2) = plt.subplots(2,1, sharex=False, figsize=(15,9))
    fig.tight_layout(pad=6.0)
    #fig.autofmt_xdate()
    #plt.figure(figsize=(10, 10))
    #plt.xticks(rotation=45)
    ax1.plot(x1,y1)
    #plt.xticks(rotation=45)
    ax1.set_title('Stock Price')
    

    #SECOND CHART
    x2 = stock_df1.index.to_numpy()
    y2=stock_df1['Volume'].to_numpy()
    #Volume bar plot
    #fig1, ax1 = plt.subplots()
    #plt.figure(figsize=(10, 10))
    #plt.xticks(rotation=45)
    ax2.bar(x2, y2)
    #plt.xticks(rotation=45)
    ax2.set_title('Volume')


 
    #plt.xticks(rotation=45)
    #plt.subplots_adjust(bottom=0.2)


    #SHOW BOTH PLOTS
    plt.show()
    
    
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig, window)  
    canvas.draw()
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()
  
    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()
  
    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()

def gen_charts2(stock_name):
    
    #IMPORTING STOCK DATA
    stock_data = yf.Ticker(stock_name)
    stock_df1 = stock_data.history(period='1mo', interval='1d')
    
    #Assigning the variables and reshaping them into a 2-D array
    x_train = np.arange(1,21).reshape(-1,1)
    y_train = np.array(stock_df1['Close'])
    
    x_pred=np.array(21).reshape(-1,1)
    #y_test = np.array(test_data['Close'])
    
    #Training the model with the variables
    lr_model = LinearRegression()
    
    lr_model.fit(x_train, y_train)
    
    y_pred = lr_model.predict(x_pred)
    
    
    ##CONVERTING THE DATE COLUMN TO DATETIME FORMAT
    
    stock_df1.index = pd.to_datetime(stock_df1.index).strftime('%Y-%m-%d %H:%M:%S')
    
    
    # get the maximum date in the column
    max_date = stock_df1.index.max()
    
    max_date = pd.to_datetime(max_date)
    
    one_day = timedelta(days=1)
    
    # calculate the next date
    next_date = max_date + one_day
    
    #next_date = pd.to_datetime(next_date).strftime('%Y-%m-%d')
    
    ######### ADD THE PREDICTED VALUE TO THE DATAFRAME ###############
    stock_df1.at[next_date, "Close"] = y_pred
    
    #CONVERTING TO DATETIME FORMAT AGAIN
    stock_df1.index = pd.to_datetime(stock_df1.index).strftime('%Y-%m-%d')
    
    #########################################
    #FINAL PLOT
    
    DF = pd.DataFrame()
    DF['value'] = stock_df1['Close'].values
    DF = DF.set_index(stock_df1.index.values)
    #plt.gcf().autofmt_xdate()
    #plt.plot(DF, 'o', color = 'blue')
    #colors = ['g'] * len(stock_df1.index.values)
    #colors[-1] = 'r'
    #plt.scatter(DF.index.values, DF['value'], c=colors)
    #plt.gcf().autofmt_xdate()
    #plt.show()
    
    ##########################################
    
    colors = ['g'] * len(stock_df1.index.values)
    colors[-1] = 'r'
    fig2, ax2 = plt.subplots(figsize=(9,9))
    ax2.scatter(DF.index.values, DF['value'], c=colors)
    ax2.set_title('Predicted Price')
    plt.gcf().autofmt_xdate()
    plt.show()
    
        
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig2, window)  
    canvas.draw()
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()
  
    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()
  
    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()

    

    
#PRESS BUTTON FUNCTION
def but_press1():
    stock_name = stock_entry.get()
    gen_charts1(stock_name)
    
def but_press2():
    stock_name = stock_entry.get()
    gen_charts2(stock_name)    
    
    
#MAIN WINDOW
window = tk.Tk()  
window.title("Price and Volume Charts") 
window.geometry("1000x1000")
label = tk.Label(window, text="")



#LABELS AND STOCK INPUT
stock_label = tk.Label(window, text = "Enter stock name in uppercase followed by '.NS' : ")
stock_label.pack()
label.pack()
stock_entry = tk.Entry(window)
stock_entry.pack()

#BUTTONS
generate_button1 = tk.Button(window, text = "Genarate Charts", command = but_press1)
generate_button1.pack()

generate_button2 = tk.Button(window, text = "Predict stock price", command = but_press2)
generate_button2.pack()



#MAIN FUNCTION
window.mainloop()
