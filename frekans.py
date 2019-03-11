def frekans (list) :
    frekans_table = {}
    for item in list :
        frekans = 0
        for item2 in list :
            if item == item2:
                frekans += 1
        #frekans_table.update ({item:frequency})
        frekans_table[item]=frekans
    return frekans_table

def frequency2(list):
    frekans_dict = {}
    for item in list :
        if (item in frekans_dict):
            frekans_dict[item] = frekans_dict[item]+1
        else:
            frekans_dict[item] = 1
    return frekans_dict

def frequency_with_list(list):
    frekans_list = []
    for i in range(len(list)):
        s = False
        for j in range(len(frekans_list)):
            if list[i] == frekans_list[j][0]:
                frekans_list[j][1] += 1
                s = True
        if not s:
            frekans_list.append([list[i],1])
    return frekans_list
