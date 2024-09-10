immutable_var=1,2,3,'a','d','e','omg'
print(immutable_var)
#immutable_var[1]=22
#print(immutable_var)
#кортеж нельзя изменить, что задумано в целях защиты изначального списка. для изменяемых списков создаем Списки с кавычками, Кортеж без кавычек, предназначен для хранения неизменяемых ни при каких обстоятельствах списков
mutable_list=[10,20,30, 'x','w','z','no']
print(mutable_list)
mutable_list[0:7]=1000,2000,3000,'a','b','c','yes'
print(mutable_list)
