import pandas as pd
from itertools import combinations
from openpyxl import Workbook

df = pd.read_excel('/home/foad/Downloads/phi-pii.xlsx')

quasi_identifiers = ['AGE', 'LOCATION', 'NRP', 'PHONE_NUMBER']
sensitive_attribute = 'DISEASES'

def calculate_reidentification_risk(df, group_columns):
    group_sizes = df.groupby(group_columns).size()
    
    reid_risks = 1 / group_sizes
    
    overall_risk = reid_risks.mean()
    
    return overall_risk, group_sizes

wb = Workbook()
ws = wb.active
ws.title = "Re-identification Risk"

ws.append(["Combination", "Group Size", "Re-identification Risk"])

for r in range(2, 5):
    for combo in combinations(quasi_identifiers, r):
        overall_risk, group_sizes = calculate_reidentification_risk(df, list(combo))
        
        for group, size in group_sizes.items():
            ws.append([', '.join(combo), str(group), 1 / size])

        ws.append(["Overall Risk for Combination", ', '.join(combo), overall_risk])

wb.save("reidentification_risk_results.xlsx")

print("Results saved to reidentification_risk_results.xlsx")
