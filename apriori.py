import pandas as pd
from apyori import apriori
store_data = pd.read_csv('Dataset.csv')
print(store_data.shape)
col = ['Left Hand Side', 'Right Hand Side', 'Support', 'Confidence', 'Lift']
records = []
for i in range(len(store_data)):
 records.append([str(store_data.values[i, j]) for j in range(0, 4)])
print(records)
rules = apriori(transactions=records, min_support=0.03, min_confidence=0.2, min_lift=3, 
min_length=2)
results = list(rules)
print(results)
def apriori(results):
 lhs = [tuple(result[2][0][0])[0] for result in results]
 rhs = [tuple(result[2][0][1])[0] for result in results]
 supports = [result[1] for result in results]
 confidences = [result[2][0][2] for result in results]
 lifts = [result[2][0][3] for result in results]
 return list(zip(lhs, rhs, supports, confidences, lifts))
resultsinDataFrame = pd.DataFrame(apriori(results), columns=col)
resultsinDataFrame.to_csv('apriori.csv', index=None)
print(resultsinDataFrame) 
