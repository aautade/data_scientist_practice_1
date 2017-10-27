food_thanksgiving = {}
for each in region:
    if pd.isnull(each):
        celebrate_thanksgiving["No Answer"] = 0
    else:
        thanks = data[data['US Region'] == each].loc[:,'What is typically the main dish at your Thanksgiving dinner?'].value_counts()
        #celebrate_thanksgiving[thanks.keys().max()] = thanks.max()
        food_thanksgiving[each] = thanks.keys().max()
        #print(thanks.keys().max())
        #break
print(food_thanksgiving)
