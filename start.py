import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
print(student_dict)

dt_arrange = pandas.DataFrame(student_dict)
print(dt_arrange)

#################################################################################################### OR #########

new_list = {new:main for (new, main) in dt_arrange.items()}
print(new_list)

####################################################################################################
# for (grade, level) in dt_arrange.items()
################################################## OR ############################
for grade, level in dt_arrange.items():
    print(grade)
    print(level)

###################################################################################################################

for (key, value) in dt_arrange.iterrows():
    print(key)
    print(value)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}