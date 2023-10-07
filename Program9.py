def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
duplicate = [12,24,35,24,88,120,155,88,120,155]
print(Remove(duplicate))