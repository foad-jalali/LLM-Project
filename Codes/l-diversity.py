import pandas as pd
from itertools import combinations
from openpyxl import Workbook

df = pd.read_excel('/home/foad/Downloads/phi-pii.xlsx')

def calculate_k_anonymity(df, identifiers):
    grouped = df.groupby(list(identifiers))
    
    group_sizes = grouped.size()
    k_anonymity = group_sizes.min()
    return k_anonymity

quasi_identifiers = ['AGE', 'LOCATION', 'NRP', 'PHONE_NUMBER']

group_sizes = [2, 3, 4]
results = {}

wb = Workbook()
ws = wb.active
ws.title = "K-Anonymity Results"

ws.append(["Combination", "K-Anonymity"])

for size in group_sizes:
    for combo in combinations(quasi_identifiers, size):
        combo_name = '-'.join(combo)
        
        k_anonymity = calculate_k_anonymity(df, combo)
        ws.append([combo_name, k_anonymity])

wb.save('k_anonymity_results.xlsx')
