
#1.

i=1

bag=""

while(i<=5):
    bag+=str(i)+" "
    print(bag)
    i+=1
 
#2.
numbers = [12, 75, 150, 180, 145, 525, 50]
    
    
for i in range(len(numbers)):
        
    if(numbers[i]%5==0):
            if(numbers[i]<=150):
                print(numbers[i])
            elif(numbers[i]>150 and numbers[i]<=500):
                continue
            elif(numbers[i]>500):
                break     
    

#3.

s1 = "Ault"
s2 = "Kelly"
def append_in_middle(s1,s2):
    middle_index = int(len(s1)/2)
    s3 = s1[:middle_index] + s2 + s1[middle_index:]
    return s3

# Example usage

s3 = append_in_middle(s1,s2)
print(s3)

#4.
str4 = "PyNaTive"
bag1=""


for i in range(len(str4)):
    
    if(str4[i].islower()):
        bag+=str4[i]
        
for i in range(len(str4)):
    
    if(str4[i].isupper()):
        bag+=str4[i] 

print(bag)          

#5.

list5 = ["M", "na", "i", "Ke"]
list4 = ["y", "me", "s", "lly"]   

def add_lists(list1, list2):
    new_list = []
    max_length = max(len(list1), len(list2))

    for i in range(max_length):
        if i < len(list1) and i < len(list2):
            new_list.append(list1[i] + list2[i])
        elif i < len(list1):
            new_list.append(list1[i])
        elif i < len(list2):
            new_list.append(list2[i])

    return new_list

# Example usage

new_list = add_lists(list5, list4)
print(new_list)


#6

list6 = ["Hello ", "take "]
list7 = ["Dear", "Sir"]

new_list6=[]

for i in range(len(list6)):
    for j in range(len(list7)):
        new_list6.append(list6[i]+list7[j])
 

print(new_list6)


#7.

list8 = [10, 20, 30, 40]
list9 = [100, 200, 300, 400]
list10 = list9[::-1]



for i in range(len(list8)):
    for j in range(len(list9)):
        if(i==j):
            print(list8[i],list10[j])
        
 


#8.

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000} 

new_dic={}  

for i in range(len(employees)):
     new_dic[employees[i]] = defaults

print(new_dic)     


#9.

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

for key in (sample_dict):
    for i  in range(len(keys)):
        if(key==keys[i]):
            print(key,sample_dict[key])
            

#10.

tuple1 = (11, [22, 33], 44, 55)     

nested_list = list(tuple1)

nested_list[1][0]=222

nested_tuple = tuple(nested_list)

print(nested_tuple)
    
    
        