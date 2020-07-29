import collections
dict1= {'day1':'mon','day2':'tue'}
dict2={'day3':'wed','day4':'thu'}
res = collections.ChainMap(dict1,dict2)
print(res)
print(res.maps,'\n')
# print('Keys={}'.format(list(res.keys())))
# print('values={}'.format(list(res.values())))
# print()
# print("elements:")
# for key,val in res.items():
#     print(f'{key}={val}')
# print()

# print('day3 in res: {}',format(('day5' in res )))

#map ordering
res2=collections.ChainMap(dict2,dict1)
print(res2.maps,'\n')

# update
dict2['day4']='fri'
print(res.maps)