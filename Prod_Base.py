import ast

# Read Base
f = open('base.txt', 'r+')
List = [line.strip() for line in f.readlines()]
f.close()

# Init Vectors
ruser=[]
n_cat=input('Enter the number of categories')

# Init Params
alpha=0.1
p=1/int(n_cat)

# Processing
for element in List:
    rec_dict={}
    for a in ast.literal_eval(str(element)):
        if a not in rec_dict.keys():
            rec_dict[a] = (1 - alpha) * p + alpha
            for e in rec_dict.keys():
                if(e!=a):
                    rec_dict[e] = (1 - alpha) * rec_dict[e]
        else:
            rec_dict[a] = (1 - alpha) * rec_dict[a] + alpha
            for e in rec_dict.keys():
                if(e!=a):
                    rec_dict[e] = (1 - alpha) * rec_dict[e]
    ruser.append(rec_dict)

# Output
for i in range(22):
    print(ruser[i])