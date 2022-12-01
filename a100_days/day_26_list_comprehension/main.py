import pandas

student_dict = {
    "student": ["Angela", "James", "Nick"],
    "score": [67, 78, 96]
}

student_data_frame = pandas.DataFrame(student_dict)

# Loop through a DataFrame
# for (key, value) in student_data_frame.items():
#     print(key)
#     print(value)

# Loop through rows of a DataFrame
for (index, row) in student_data_frame.iterrows():
    print(row.student, row.score)
