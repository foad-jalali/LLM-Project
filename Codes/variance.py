import pandas as pd
import numpy as np

file_path = 'files-specific-3.5/delta_disclosure_results-GPT3.5.xlsx' 
df = pd.read_excel(file_path)

if 'Combination' in df.columns and 'Delta Disclosure' in df.columns:
    stats = df.groupby('Combination').agg(
        max_value=('Delta Disclosure', 'max'),
        min_value=('Delta Disclosure', 'min'),
        mean_value=('Delta Disclosure', 'mean'),
        median_value=('Delta Disclosure', 'median'),
        var_value=('Delta Disclosure', 'var'),
        std_value=('Delta Disclosure', 'std')
    ).round(2)


    print(stats)
output_df = pd.DataFrame(stats)
output_df.to_excel('files-specific-3.5/newdelta_disclosure_results-GPT3.5.xlsx', index=False)
