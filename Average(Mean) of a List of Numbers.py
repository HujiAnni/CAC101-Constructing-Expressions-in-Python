# define a list of numbers and assign it to my_list
my_list = [10,20,30,40]

# Set a running total for elements in the list, initialized to 0
total = 0
# Set a counter for the number of elements in the list, initialized to 0
num_elements = 0

# Loop over all the elements in the list
for element in my_list:
    # Add the value of the current element to total
    total = total + element
    # Add 1 to our counter num_elements
    num_elements = num_elements + 1

# Compute the average by dividing the total by num_elements
average = total / num_elements


my_list_average=sum(my_list)/len(my_list)
print(my_list_average)



my_set={40,20,30,10}
my_set_average=sum(my_set)/len(my_set)
print(my_set_average)
