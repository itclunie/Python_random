import pandas as pd


df = pd.read_excel("/Users/itclunie/Downloads/RFT_contract_tracking.xlsx", header=[0])


#make each row a series. can call on values by column header
for i in range(len(df)):
    row = df.iloc[i]    
    print(row["Last Name"], row["First Name"], row["January Hours"])
    
