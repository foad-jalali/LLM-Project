import pandas as pd
from collections import Counter

categories = {
    "(Cancer-related)": ["cancer", "tumor", "lymphoma", "melanoma"],
    "(Metabolic Disorders)": ["diabetes", "weight loss", "thyroid", "metabolic"],
    "(Infectious Diseases)": ["infection", "virus", "bacterial", "HIV", "COVID", "endometriosis"],
    "(Cardiovascular)": ["heart", "cardio", "hypertension", "stroke"],
    "(Dermatological)": ["skin", "eczema", "psoriasis", "rash"],
    "(Gastrointestinal)": ["stomach", "gastric", "ulcer", "intestinal", "liver"],
    "(Respiratory Disorders)": ["respiratory", "asthma", "lung", "bronchitis"],
    "(Neurological)": ["anxiety", "neuro", "epilepsy", "migraine"],
    "(Renal Disorders)": ["kidney", "renal", "nephritis"],
    "(Other)": [] 
}

def classify_disease(disease_name):
    for category, keywords in categories.items():
        if any(keyword in disease_name.lower() for keyword in keywords):
            return category
    return "(Other)"

df = pd.read_excel(file_path)

df['Disease'] = df['Disease'].fillna('').astype(str)

df['Category'] = df['Disease'].apply(classify_disease)

df.to_excel(output_path, index=False)
print(f"داده‌ها با موفقیت دسته‌بندی و ذخیره شدند: {output_path}")

medication_categories = {
    "(Analgesics)": ["paracetamol", "ibuprofen", "naproxen", "acetaminophen"],
    "(Antibiotics)": ["amoxicillin", "ciprofloxacin", "doxycycline", "penicillin"],
    "(Cardiovascular Drugs)": ["amlodipine", "atorvastatin", "aspirin", "clopidogrel"],
    "(Anti-Cancer Drugs)": ["methotrexate", "paclitaxel", "tamoxifen", "imatinib"],
    "(Metabolic Drugs)": ["insulin", "metformin", "glyburide", "glibenclamide"],
    "(Respiratory Drugs)": ["salmeterol", "budesonide", "montelukast", "fluticasone"],
    "(Psychiatric Drugs)": ["sertraline", "alprazolam", "lamotrigine", "fluoxetine"],
    "(Others)": []
}

def classify_medication(medication_name):
    for category, keywords in medication_categories.items():
        if any(keyword in medication_name.lower() for keyword in keywords):
            return category
    return "(Others)"

file_path = '/home/foad/Projects/llm/files/gpt-3.5/count.xlsx'
df = pd.read_excel(file_path)

df['medications'] = df['Medication'].fillna('').astype(str)

df['Category'] = df['medications'].apply(classify_medication)

output_path = '/home/foad/Projects/llm/files/gpt-3.5/new/classified_medications.xlsx'
df.to_excel(output_path, index=False)
print(f"Classified medications saved to: {output_path}")