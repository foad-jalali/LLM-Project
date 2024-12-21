import pandas as pd
import spacy
from transformers import pipeline

nlp = spacy.load("en_core_web_sm")

classifier = pipeline('zero-shot-classification', model="facebook/bart-large-mnli")

categories = [
    "Pain-related", "Infections", "Cancer", "Mental Health", "Cardiovascular", "Diabetes", "Skin",
    "Gastrointestinal", "Thyroid", "Blood", "Neurological", "Respiratory", "Bone & Joint", "Liver", "Kidney", 
    "Eye", "Autoimmune"
]

def categorize_text_with_bert(text, categories):
    result = classifier(text, candidate_labels=categories)
    return result['labels'][0], result['scores'][0]

df = pd.read_excel(r"C:\\Users\\Foad\\Pictures\\files\\newphi-3.5.xlsx")

def process_text(row):
    diseases = row['Diseases']
    if isinstance(diseases, str):
        category, confidence = categorize_text_with_bert(diseases, categories)
        return category, confidence
    return None, 0

df[['Predicted Category', 'Confidence']] = df.apply(process_text, axis=1, result_type='expand')

print(df[['Diseases', 'Predicted Category', 'Confidence']])

df.to_excel(r"C:\\Users\\Foad\\Pictures\\files\\categorized-newphi-3.5.xlsx", index=False)
