celebrate_thanksgiving = {}
for each in region:
    if pd.isnull(each):
        celebrate_thanksgiving["No Answer"] = 0
    else:
        thanks = data[data['US Region'] == each].loc[:,'Do you celebrate Thanksgiving?']
        celebrate_thanksgiving[each] = thanks.value_counts()[0]
print(celebrate_thanksgiving)
