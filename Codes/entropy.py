import numpy as np
import pandas as pd

categories = [
    'Age-Location', 'Age-NRP', 'Age-Phone Number', 'Location-NRP', 
    'Location-Phone Number', 'NRP-Phone Number', 'Age-Location-NRP', 
    'Age-Location-Phone Number', 'Location-NRP-Phone Number'
]

P_discloser = [0.868, 0.882, 0.496, 0.792, 0.704, 0.4, 0.556, 0.4, 0.4]
P_non_discloser = [0.132, 0.118, 0.504, 0.208, 0.296, 0.6, 0.444, 0.6, 0.6]

def calculate_entropy(p_discloser, p_non_discloser):
    entropy = 0
    if p_discloser > 0:
        entropy -= p_discloser * np.log2(p_discloser)
    if p_non_discloser > 0:
        entropy -= p_non_discloser * np.log2(p_non_discloser)
    return entropy

entropies = [
    calculate_entropy(P_discloser[i], P_non_discloser[i])
    for i in range(len(categories))
]

df = pd.DataFrame({
    'Category': categories,
    'P-Discloser': P_discloser,
    'P-Non Discloser': P_non_discloser,
    'Entropy': entropies
})

df.to_excel('entropy_results4.0.xlsx', index=False)

print("Results saved to 'entropy_results4.0.xlsx'")
