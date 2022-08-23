import pandas as pd
uri = "https://raw.githubusercontent.com/fivethirtyeight/data/master/murder_2016/murder_2015_final.csv"
murder = pd.read_csv(uri, error_bad_lines=False, encoding='latin-1')
murder.head()

murder.plot(kind='hist')
