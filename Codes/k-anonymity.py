import pandas as pd
from openpyxl import Workbook

df = pd.read_excel(r"C:\\Users\\Foad\\Pictures\\files\\3.5.xlsx")

quasi_identifiers = ['Age', 'Location', 'NRP', 'Phone Number']

def calculate_k_anonymity(df, group_columns):
    group_sizes = df.groupby(group_columns).size()
    
    # k-anonymity برابر با حداقل تعداد رکوردها در هر گروه است
    k_anonymity = group_sizes.min()
    
    return k_anonymity, group_sizes

wb = Workbook()
ws = wb.active
ws.title = "K-Anonymity"

ws.append(["Combination", "Group", "Group Size", "K-Anonymity"])

k_anonymity, group_sizes = calculate_k_anonymity(df, quasi_identifiers)

for group, size in group_sizes.items():
    ws.append([', '.join(quasi_identifiers), str(group), size, k_anonymity])

ws.append(["Overall K-Anonymity for Quasi-Identifiers", ', '.join(quasi_identifiers), "", k_anonymity])

wb.save("k_anonymity_results.xlsx")

print("Results saved to k_anonymity_results.xlsx")
