import pandas as pd 
df = pd.read_excel(
    "data/Call-Center-Sentiment-Sample-Data.xlsx",
    header=5
    )
df = df.loc[:, ~df.columns.str.contains("^Unnamed")] #the "~" is removing what im searching for in this case UNnamed metadata that cluters

df = df.dropna(how="all") #to remove empty rows

print(df)

#counts amount of each given senitment type
ver_pos = len(df[df["Sentiment"] == "Very Positive"]) #alternativly could use:  ver_pos = (df["Sentiment"] == "Very Positive").sum()
print(ver_pos)

pos = len(df[df["Sentiment"] == "Positive"]) 
print(pos)

neut = len(df[df["Sentiment"] == "Neutral"]) 
print(neut)

neg = len(df[df["Sentiment"] == "Negative"]) 
print(neg)

ver_neg = len(df[df["Sentiment"] == "Very Negative"]) 
print(ver_neg)