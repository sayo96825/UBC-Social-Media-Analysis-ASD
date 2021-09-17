sortable = [4,"s",3,"a",7, 9,"y","o"]
print(sortable)

int_list = [x for x in sortable if isinstance(x,int)]
int_list.sort()
print(int_list)
