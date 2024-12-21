import pandas as pd
from itertools import combinations
import numpy as np
from scipy.stats import entropy
from openpyxl import Workbook

df = pd.read_excel('/home/foad/Downloads/phi-pii.xlsx')

def calculate_distribution(series):
    distribution = series.value_counts(normalize=True)
    return distribution

def kl_divergence(p, q):
    p = p.reindex(q.index, fill_value=0)
    q = q.reindex(p.index, fill_value=0)
    return entropy(p, q)

def calculate_t_closeness(df, identifiers, sensitive_attr, global_distribution):
    t_closeness = {}
    grouped = df.groupby(list(identifiers))
    
    for group, data in grouped:
        group_distribution = calculate_distribution(data[sensitive_attr])
        t_closeness_value = kl_divergence(group_distribution, global_distribution)
        t_closeness[group] = t_closeness_value
    
    return t_closeness

quasi_identifiers = ['AGE', 'LOCATION', 'NRP', 'PHONE_NUMBER']
sensitive_attr = 'DISEASES'

global_distribution = calculate_distribution(df[sensitive_attr])

group_sizes = [2, 3, 4]
results = {}

for size in group_sizes:
    for combo in combinations(quasi_identifiers, size):
        combo_name = '-'.join(combo)
        t_closeness = calculate_t_closeness(df, combo, sensitive_attr, global_distribution)
        results[combo_name] = t_closeness

wb = Workbook()
ws = wb.active
ws.title = "T-Closeness Results"
ws.append(["Combination", "Group", "T-Closeness"])
for group_size, t_closenesses in results.items():
    for group, t_value in t_closenesses.items():
        ws.append([group_size, str(group), t_value])
wb.save('t_closeness_results.xlsx')
