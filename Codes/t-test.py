import pandas as pd
import numpy as np
from scipy import stats

data_35 = {
    'Combination': [
        'Age-Location', 'Age-Location-Phone Number', 'Age-NRP', 'Age-Phone Number',
        'Location-NRP', 'Location-Phone Number', 'NRP-Phone Number'
    ],
    'Mean': [10546.57, 0.00, 12617.48, 0.00, 8307.58, 5197.50, 0.00],
    'Variance': [87817999.30, 0.00, 73045484.39, 0.00, 74500233.01, 59139770.70, 0.00],
    'N': [44, 1, 20, 2, 28, 6, 1]
}

data_40 = {
    'Combination': [
        'Age-Location', 'Age-Location-Phone Number', 'Age-NRP', 'Age-Phone Number',
        'Location-NRP', 'Location-Phone Number', 'NRP-Phone Number', 'Age-Location-NRP', 'Location-NRP-Phone Number'
    ],
    'Mean': [9714.79, 1766.55, 0.00, 12915.67, 303.30, 7431.77, 0.00, 5184.40, 0.00],
    'Variance': [82139183.20, 0.00, 0.00, 81355520.72, 183977.99, 77654734.86, 0.00, 71397936.80, 0.00],
    'N': [50, 1, 19, 2, 37, 5, 2, 1, 1]  # تعداد نمونه‌ها برای هر ترکیب
}
df_35 = pd.DataFrame(data_35)
df_40 = pd.DataFrame(data_40)

df_combined = pd.merge(df_35, df_40, on='Combination', how='outer', suffixes=('_35', '_40'))

results = []
for index, row in df_combined.iterrows():
    mean_1 = row['Mean_35']
    var_1 = row['Variance_35']
    n_1 = row['N_35']
    
    mean_2 = row['Mean_40']
    var_2 = row['Variance_40']
    n_2 = row['N_40']
    
    if (var_1 == 0 and var_2 == 0) or (n_1 == 1 and n_2 == 1):
        t_statistic = 0
        p_value = 1.0
    else:
        pooled_variance = ((n_1 - 1) * var_1 + (n_2 - 1) * var_2) / (n_1 + n_2 - 2)
        t_statistic = (mean_1 - mean_2) / np.sqrt(pooled_variance * (1/n_1 + 1/n_2))
        df = n_1 + n_2 - 2
        
        p_value = stats.t.sf(np.abs(t_statistic), df) * 2
    
    results.append({
        'Combination': row['Combination'],
        'T-Statistic': t_statistic,
        'p-Value': p_value,
        'Mean (GPT-3.5)': mean_1,
        'Mean (GPT-4)': mean_2
    })

results_df = pd.DataFrame(results)
print(results_df)
results_df.to_excel('delta_disclosure_results_t_test.xlsx', index=False)
