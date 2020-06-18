import pandas as pd

df1 = pd.read_csv("new_bipartisan.csv", index_col=[0])
df2 = pd.read_csv("new_breitbart.csv", index_col=[0])
df3 = pd.read_csv("new_knowhere.csv", index_col=[0])
df4 = pd.read_csv("new_nypost.csv", index_col=[0])
df5 = pd.read_csv("new_foxnews.csv", index_col=[0])
out1 = df1.append(df2, ignore_index = True)
out2 = df3.append(df4, ignore_index = True)
out3 = out1.append(out2, ignore_index = True)
out = out3.append(df5, ignore_index = True)
out.to_csv("final_record.csv")

print("Wooohhoooo Done !!!!!!!!!")