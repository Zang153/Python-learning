test_list = ['first', 'second']
copy_list = test_list
print(f'This is the copy list {copy_list}.')
test_list.insert(5,'test')
print(test_list)
test_list.remove('first')
print(test_list)
print(len(test_list))
print(sorted(test_list,reverse=False))
