sortable = [4,"s",3,"a",7, 9,"y","o"]
print(sortable)

int_list = [x for x in sortable if isinstance(x,int)]
String_list = [x for x in sortable if isinstance(x,str)]
int_list.sort()
String_list.sort()
print(int_list)
print(String_list)
