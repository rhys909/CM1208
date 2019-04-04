import numpy as np
from itertools import zip_longest


#Reads the history file and generates a list
hist_file = open("history.txt", "r")
hist_content = hist_file.read().split()
No_Customers = hist_content[0]
No_Items = hist_content[1]
No_Trans = hist_content[2]
hist_content.pop(0)
hist_content.pop(0)
hist_content.pop(0)
hist_file.close()

def read_cart():
    cart_file = open("queries.txt", "r")
    cart_content = cart_file.readlines()
    cart_list = [i.strip() for i in cart_content]
    return cart_list


item_list = []
customer_list = []
count = 0
for i in hist_content:
    if count % 2 == 0:
        customer_list.append(hist_content[count])
        count += 1
    elif count % 2 == 1:
        item_list.append(hist_content[count])
        count += 1

# x is the item which vector is to be calculated
def calc_vector(x):
    item_vector = []
    count = 0
    for count in range(0, int(No_Customers)):
        item_vector.append(0)
    for i in item_list:
        if i == x:
            
    return item_vector

def calc_angle(a, b):
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    cos_theta = np.dot(a, b) / (norm_a * norm_b)
    theta = math.degrees(math.acos(cos_theta))
    return theta

def average_angle():
    return 35


def entries():
    return int(No_Customers) + int(No_Items)

def cart_calculator():
    hist_list = read_history()
    cart_list = read_cart()

print(hist_content)
print(customer_list)
print(item_list)
item_vector = calc_vector()
print(item_vector)
cart_list = read_cart()
print(cart_list)
pos_entries = entries()

print("Positive entries: " + str(pos_entries))
#average angle printed out

print("Average angle: ")
#for loop which calculates the
