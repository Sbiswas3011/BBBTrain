import pandas as pd
import json 

cleaned_file_path = 'BBB_Data/CleanedData.csv'

cleaned_df = pd.read_csv(cleaned_file_path)

for i,row in cleaned_df.iterrows():
    rowdata = json.loads(row['AA_Percentages'].replace("'", "\""))
    cleaned_df['A'] = rowdata['A']
    cleaned_df['C'] = rowdata['C']
    cleaned_df['D'] = rowdata['D']
    cleaned_df['E'] = rowdata['E']
    cleaned_df['F'] = rowdata['F']
    cleaned_df['G'] = rowdata['G']
    cleaned_df['H'] = rowdata['H']
    cleaned_df['I'] = rowdata['I']
    cleaned_df['K'] = rowdata['K']
    cleaned_df['L'] = rowdata['L']
    cleaned_df['M'] = rowdata['M']
    cleaned_df['N'] = rowdata['N']
    cleaned_df['P'] = rowdata['P']
    cleaned_df['Q'] = rowdata['Q']
    cleaned_df['R'] = rowdata['R']
    cleaned_df['S'] = rowdata['S']
    cleaned_df['T'] = rowdata['T']
    cleaned_df['V'] = rowdata['V']
    cleaned_df['W'] = rowdata['W']
    cleaned_df['Y'] = rowdata['Y']

cleaned_df = cleaned_df.drop(columns=['AA_Counts', 'AA_Percentages'])

cleaned_df.to_csv("BBB_Data/ReadyData.csv", index=False)