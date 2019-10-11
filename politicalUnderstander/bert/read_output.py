import pandas as pd
#read the original test data for the text and id 
df_test = pd.read_csv('dataset/test.tsv', sep='\t')
#read the results data for the probabilities
df_result = pd.read_csv('bert_output/test_results.tsv', sep='\t', header=None)
#create a new dataframe
df_map_result = pd.DataFrame({'guid': df_test['guid'],
'text': df_test['text'],
'label': df_result.idxmax(axis=1)})
#view sample rows of the newly created dataframe 
print(df_map_result.sample(10))
