import statsmodels.api as sm

from statsmodels.tsa.arima.model import ARIMA

arma_mod20 = ARIMA(df['Open'], order=(1, 1, 10)).fit()

y=arma_mod20.predict(start=0,end=len(df)-1)

plt.plot(df['index'],y,color='r')
plt.plot(df['index'],df['Open'])

arma_mod20 = ARIMA(df['Open'], order=(1, 1, 10)).fit()

y=arma_mod20.predict(start=0,end=2*len(df)-1)
x=[i for i in range(0,2*len(df))]

plt.plot(x,y,color='r')
