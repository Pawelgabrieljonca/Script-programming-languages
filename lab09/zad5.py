import pandas as pd
# Wczytanie pliku CSV z separatorem tabulatora
df = pd.read_csv("oceny.csv", sep='\t')
# Sprawdzenie nazw kolumn i pierwszych wierszy
print("Nazwy kolumn w DataFrame:", df.columns)
print(df.head())
# Najniższa ocena z laboratoriów dla każdego studenta
df['Min_LAB'] = df[['Lab1', 'Lab2', 'Lab3', 'Lab4', 'Lab5']].min(axis=1)
print("Najniższa ocena z laboratoriów dla każdego studenta:")
print(df[['Min_LAB']])
# Średnia ocena z egzaminu
average_exam = df['Exam'].mean()
print(f"Średnia ocena z egzaminu: {average_exam:.2f}")
# Liczba 2 z egzaminu
count_exam_2 = (df['Exam'] == 2).sum()
print(f"Liczba ocen 2 z egzaminu: {count_exam_2}")
# Czy jest student, który miał same 5 z laboratoriów
all_5_in_labs = any((df[['Lab1', 'Lab2', 'Lab3', 'Lab4', 'Lab5']] == 5).all(axis=1))
print(f"Czy jest student, który miał same 5 z laboratoriów: {'Tak' if all_5_in_labs else 'Nie'}")
# Czy jest student, który miał 2 z Lab2 i Lab3
student_2_in_lab2_lab3 = any((df['Lab2'] == 2) & (df['Lab3'] == 2))
print(f"Czy jest student, który miał 2 z Lab2 i Lab3: {'Tak' if student_2_in_lab2_lab3 else 'Nie'}")
# Liczba studentów, którzy dostali wyższą ocenę z egzaminu niż średnia z laboratoriów
df['Average_LAB'] = df[['Lab1', 'Lab2', 'Lab3', 'Lab4', 'Lab5']].mean(axis=1)
students_higher_exam = (df['Exam'] > df['Average_LAB']).sum()
print(f"Liczba studentów, którzy dostali wyższą ocenę z egzaminu niż średnia z laboratoriów: {students_higher_exam}")
# Liczba piątek uzyskanych przez studenta z największą liczbą 5
df['Count_5'] = (df[['Lab1', 'Lab2', 'Lab3', 'Lab4', 'Lab5', 'Exam']] == 5).sum(axis=1)
max_5_student = df['Count_5'].max()
print(f"Liczba piątek uzyskanych przez studenta z największą liczbą 5: {max_5_student}")



