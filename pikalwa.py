import pandas as pd
import pickle


with open('kuch.pkl', 'rb') as f:
    data = pickle.load(f)
print(data)
df=pd.DataFrame(data)
df.to_csv("pickle_ka_data.csv")