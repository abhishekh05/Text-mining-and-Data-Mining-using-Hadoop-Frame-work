import sys


f = open(sys.argv[1],"r")

contents = f.read()

def concatenate_list_data(list):
    result= ''
    for element in list:
        result += str(" ")+ str(element)
    return result


for line in contents:


	print(line[0])
	

f.close()