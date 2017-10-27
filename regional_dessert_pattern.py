region_pattern = {}
region_dessert = {}
dessert = {}
cols = data.columns
cols = cols.tolist()
cols_dessert = []
for each in cols:
    if each.startswith("Which of these desserts"):
        cols_dessert.append(each)
region = data['US Region'].unique().tolist()
for each in region:
    new_list = []
    if pd.isnull(each):
        each = "U.S.A."
    else:
        each = each
    single_region = data['US Region'] == each
    for row in cols_dessert:
        if "Other" in row:
            key = data[single_region][row].value_counts().keys().tolist()
            val = data[single_region][row].value_counts().tolist()
            ditt = dict(zip(key,val))
            mapp = map(key,value)
            new_list.append(ditt)
            region_pattern[each] = new_list
        else:
            key = data[single_region][row].value_counts().keys().tolist()
            val = data[single_region][row].value_counts().tolist()
            ditt = dict(zip(key,val))
            mapp = map(key,value)
            new_list.append(ditt)
            region_pattern[each] = new_list
        #break
    #break
print(region_pattern)
