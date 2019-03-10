def frequency (list) :
    freq_table = {}
    for item in list :
        frekans = 0
        for item2 in list :
            if item == item2:
                frekans += 1
        #freq_table.update ({item:frequency})
        freq_table[item]=frekans
    return freq_table





def frequency2(list):
    freq_dict = {}
    for item in list :
        if (item in freq_dict):
            freq_dict[item] = freq_dict[item]+1
        else:
            freq_dict[item] = 1
    return freq_dict

def frequency_with_list(list):
    frequency_list = []
    for i in range(len(list)):
        s = False
        for j in range(len(frequency_list)):
            if list[i] == frequency_list[j][0]:
                frequency_list[j][1] += 1
                s = True
        if not s:
            frequency_list.append([list[i],1])
    return frequency_list