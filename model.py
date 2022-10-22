import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import adfuller
from sklearn import metrics
import matplotlib.pyplot as plt
import statsmodels.api as sm
from pandas.tseries.offsets import DateOffset

#Stationarity check using dickey fuller test
def adfuller_test(sales,df):
    res=adfuller(sales)
    labels=['ADF test statistic','p-value','Lags used','Number of Observation used']
    for values,label in zip(res,labels):
        print(label+" : "+str(values))
    if(res[1] <= 0.05):
        print("Data has no root unit and is stationary")
    else:
        df['Sales first difference'] = df['Sales'] - df['Sales'].shift(1)
        df['Sales Seasonal difference'] = df['Sales'] - df['Sales'].shift(12)
        #df['Sales Seasonal difference'].plot()
        

def model(path,period,date):
    res=[]
    df=pd.read_csv(path)
    period=period
    df.columns=['Month','Sales']
    df.drop(106,axis=0,inplace=True)
    df.drop(105,axis=0,inplace=True)

    df['Month']=pd.to_datetime(df['Month'])
    df.set_index('Month', inplace=True)

    #Data Virtualization
    #df.plot()
    adfuller_test(df['Sales'],df)
    
    #Fitting into model
    model=sm.tsa.statespace.SARIMAX(df['Sales'],order=(1, 1, 1),seasonal_order=(1,1,1,12)) #p,d,q
    results=model.fit()
    print(results.summary().tables[1])

    #Testing model
    df['forecast']=results.predict(start=90,end=103,dynamic=True)
    df[['Sales','forecast']].plot(figsize=(7,4))
    df.to_csv(r'./files/updated-dataset.csv')

    test=[]
    predictions=[]

    for i in range(90,103):
        test.append(df['Sales'][i])
        predictions.append(df['forecast'][i])
    MAE = metrics.mean_absolute_error(test, predictions)
    MAPE = metrics.mean_absolute_percentage_error(test, predictions)
    Rmse = np.sqrt(metrics.mean_squared_error(test, predictions))
    print("MAE : "+str(MAE))
    print("MAPE : "+str(MAPE))
    print("RMSE : "+str(Rmse))
    res.append(MAE)
    res.append(MAPE)
    res.append(Rmse)
    df.tail(20)

    if(period == 'monthly'):
        end_value=104+int(date)
        end_month=int(date)
    else:
        end_month=(int(date)*12)+4
        end_value=104+end_month
    future_dates=[df.index[-1]+DateOffset(months=x)for x in range(0,end_month)]
    future_dates_df=pd.DataFrame(index=future_dates[1:],columns=df.columns)
    future_df=pd.concat([df,future_dates_df])
    if(period == 'monthly'):
        future_df['forecast']=results.predict(start=104,end=end_value,dynamic=True)
        #plotting
        future_df.index.name = 'Month'
        fig = plt.figure(figsize=(7,4))
        plt.plot(future_df[['Sales','forecast']])
        plt.ylabel("Sales")
        plt.show()
        fig.savefig('./graph/predicted.png')
        #future_df.tail(30)

    else:
        future_df['forecast']=results.predict(start=96,end=end_value,dynamic=True)
        future_df.tail()
        #grouping monthly predicted to yearly
        future_df['Year']=future_df.index
        future_df.Year=future_df.Year.apply(lambda x:x.year)
        future_df_yearly=future_df.groupby('Year')['Sales'].sum().reset_index()
        future_df1_sales=future_df.groupby('Year')['forecast'].sum().reset_index()
        future_df_yearly['forecast']=future_df1_sales['forecast'] 
        future_df_yearly['Sales'][8]=future_df_yearly['forecast'][8]
        #plotting
        future_df_yearly['Sales']=future_df_yearly['Sales'].replace(0, np.nan)
        future_df_yearly['forecast']=future_df_yearly['forecast'].replace(0, np.nan)
        future_df_yearly.set_index('Year',inplace=True)
        fig = plt.figure(figsize=(7,4))
        plt.plot(future_df_yearly[['Sales','forecast']])
        plt.ylabel("Sales")
        plt.show()
        fig.savefig('./graph/predicted.png')
        print(future_df_yearly)
    return res