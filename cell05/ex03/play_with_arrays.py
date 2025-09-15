ls = [2,8,9,48,8,22,-12,2]
sec_ls = [x for x in ls if x > 5]
third_ls = [x+2 for x in sec_ls]
set_ls = set(third_ls)
print(set_ls)