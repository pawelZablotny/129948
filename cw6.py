import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ts = pd.Series(np.random.randn(1000))
ts = ts.cumsum()
print(ts)
ts.plot()
plt.show()

grupa = df.groupby(['Kontynent']).agg({'Populacja': ['sum']})
print(grupa)
grupa.plot(kind='bar', xlabel='Kontynent', ylabel='Mld', rot=0, legend=True,
           title='Populacja z podzialem na kontynenty')
wykre