#1.

list1=[("John", 25), ("Jane", 30)]

for name, age in list1:
    print("Name:", name)
    print("Age:", age)
 
 
#2.

dic2={}
print(dic2)

dic2["name"]="John"
dic2["age"]=25    

#print(dic2)

dic2["age"]=26

print(dic2)

dic2.clear()

print(dic2)


#3.

Input= [2,7,11,15]
target = 9

for i in range(len(Input)):
    for j in range(len(Input)):
        if(int(Input[i]+Input[j])==target):
            print(i,j)


#4.

str4="madam"   
def is_palindrome(string):
    # Remove any whitespace and convert to lowercase
    
    # Compare the string with its reverse
    return string == string[::-1]

# Example usage

if is_palindrome(str4):
    print(f"{str4} is a palindrome")
else:
    print(f"{str4} is not a palindrome")
    
    
#5.

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        # Find the minimum element in the remaining unsorted portion of the array
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the minimum element with the current element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


list = [64, 25, 12, 22, 11]
sorted_array = selection_sort(list)
print(sorted_array)


#6.

from queue import LifoQueue

class Stack:
    def __init__(self):
        self.queue = LifoQueue()

    def push(self, item):
        self.queue.put(item)

    def pop(self):
        if not self.empty():
            return self.queue.get()
        else:
            raise IndexError("Stack is empty")

    def top(self):
        if not self.empty():
            return self.queue.queue[-1]
        else:
            raise IndexError("Stack is empty")

    def empty(self):
        return self.queue.empty()

    def size(self):
        return self.queue.qsize()


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.top())  
print(stack.pop())  
print(stack.empty())  
print(stack.size())  



#7.

i=1

list7=[]

while(i<=100):
    
    if(i%3==0):
        list7.append("Fizz")
    elif(i%5==0):
        list7.append("Buzz")
    elif(i%3==0 and i%5==0):
        list7.append("FizzBuzz")
    else:
        list7.append(i)   
    i+=1 
    
    
print(list7)    
    
    
    
#8.

def count_words(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        word_count = len(content.split())

    return word_count

def write_count_to_file(word_count, output_file_path):
    with open(output_file_path, 'w') as file:
        file.write(str(word_count))


input_file_path = 'input.txt'
output_file_path = 'output.txt'

word_count = count_words(input_file_path)
write_count_to_file(word_count, output_file_path)


#9.

def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
numerator = 10
denominator = 5

result = divide_numbers(numerator, denominator)
if result is not None:
    print(f"Result: {result}")



            
                

    
         