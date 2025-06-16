import pandas as pd
import random

names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
subjects = ['Math', 'Science', 'History', 'English', 'Biology', 'Physics', 'Chemistry', 'Social', 'Geograaphy', 'Environments']
scores = [random.randint(50, 100) for _ in range(10)]

df = pd.DataFrame({
    'Name': names,
    'Subject': subjects,
    'Score': scores,
    'Grade': [''] * 10
})

def assign_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

df['Grade'] = df['Score'].apply(assign_grade)

print("Sorted by Score (Descending):")
print(df.sort_values(by='Score', ascending=False))

print("\nAverage Score by Subject:")
print(df.groupby('Subject')['Score'].mean())

def pandas_filter_pass(dataframe):
    return dataframe[dataframe['Grade'].isin(['A', 'B'])]

passed_students = pandas_filter_pass(df)
print("\nStudents with Grade A or B:")
print(passed_students)