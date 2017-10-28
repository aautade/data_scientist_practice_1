import numpy as np
cols = data.columns
cols_dessert_list = []
dessert_dict = {}
region_dict = {}

for each in cols:
    if each.startswith("Which of these desserts"):
        if "Other" in each:
            pass
        else:
            cols_dessert.append(each)
            cols_dessert_list.append(each.split("- ")[1])
region = data[data['US Region'].notnull()]['US Region'].unique().tolist()
val = []
for each in region:
    dessert_dict = {}
    for row in cols_dessert:
        val = data[data['US Region'] == each][row].value_counts().tolist()
        if not val:
            val.append(0)
        dessert_type = row.split("- ")[1]
        dessert_dict[dessert_type] = val[0]
    region_dict[each] = dessert_dict
new_df = pd.DataFrame.from_dict(region_dict)
print(new_df) 
