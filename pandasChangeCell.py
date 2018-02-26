MD = {'a':[1,2,3],'b':[4,5,6],'c':[7,8,9]}
MD['blah'] = 0
tdf = pd.DataFrame.from_dict(MD)

keepMe = [1,4,8]

for i in range(len(tdf)):
    row = tdf.iloc[i]    
    
    if i in keepMe:
        tdf.at[i,'blah'] = 2
    
tdf
