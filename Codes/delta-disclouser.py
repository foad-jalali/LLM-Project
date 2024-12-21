import pandas as pd
import numpy as np
from itertools import combinations
from openpyxl import Workbook

df = pd.read_excel('/home/foad/Downloads/phi-pii.xlsx')

quasi_identifiers = ['AGE', 'LOCATION', 'NRP', 'PHONE_NUMBER']
sensitive_attribute = 'DISEASES'

total_distribution = df[sensitive_attribute].value_counts(normalize=True)

def calculate_delta_disclosure(group):
    group_distribution = group[sensitive_attribute].value_counts(normalize=True)
    
    delta = 0
    for disease in group_distribution.index:
        p_i_G = group_distribution[disease]
        p_i_T = total_distribution.get(disease, 0)  # اگر بیماری در دیتاست کلی نباشد، 0 در نظر گرفته می‌شود
        delta = max(delta, abs(p_i_G / p_i_T - 1) if p_i_T > 0 else 0)
    
    return delta

wb = Workbook()
ws = wb.active
ws.title = "Delta Disclosure"

ws.append(["Combination", "Group", "Delta Disclosure"])

for r in range(2, 5):
    for combo in combinations(quasi_identifiers, r):
        grouped = df.groupby(list(combo))
        
        for group, group_data in grouped:
            delta = calculate_delta_disclosure(group_data)
            
            ws.append([', '.join(combo), str(group), delta])

wb.save("delta_disclosure_results.xlsx")

print("Results saved to delta_disclosure_results.xlsx")
