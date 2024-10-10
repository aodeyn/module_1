immutable_var=(1,2,3,4,5,'string1',[6,7,8])
print(immutable_var)
#immutable_var=[4]=9
#    immutable_var=[4]=9
#                   ^
#    цифры и строки являются не изменяемыми в кортеже
#SyntaxError: cannot assign to literal
mutable_list=[1,2,3,4,5,'string1',[6,7,8]]
mutable_list[0]=9
mutable_list[5]="string2"
mutable_list[4]="string1"
mutable_list[6][1]=5
print(mutable_list)

