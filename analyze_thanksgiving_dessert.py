import pandas as pd
data = pd.read_csv("thanksgiving.csv",encoding="Latin-1")
cols = data.columns.tolist()
cols_dessert = []
for each in cols:
    if each.startswith("Which of these dessert"):
        cols_dessert.append(each)
dessert = {}
for each in cols_dessert:
    dessert_type = each.split("- ")[1]
    dessert_value = data[each].value_counts().tolist()
    #print(dessert_value[0])
    dessert[dessert_type] = dessert_value[0]
print(dessert)
print("Adding a line for test branch")
