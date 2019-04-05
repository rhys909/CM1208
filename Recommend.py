import numpy as np
import math


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
cust_list = []
count = 0
for i in hist_content:
    if count % 2 == 0:
        cust_list.append(hist_content[count])
        count += 1
    elif count % 2 == 1:
        item_list.append(hist_content[count])
        count += 1
customers = []
x = 1
for x in range(1, int(No_Customers) + 1):
    customers.append(x)
    x += 1

# x is the item which vector is to be calculated
def generate_vector():
    vectors = []
    count = 0
    for i in range(0, int(No_Items)):
        vectors.append([])
        for i in range(0, int(No_Customers)):
            vectors[count].append(0)
        count += 1
    for i in range(0, len(item_list)):
        item = int(item_list[i]) - 1
        customer = int(cust_list[i]) - 1
        vectors[item][customer] = 1
    return vectors

def calc_angle(a, b):
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    cos_theta = np.dot(a, b) / (norm_a * norm_b)
    theta = round((math.degrees(math.acos(cos_theta))), 2)
    return theta

def average_angle():
    angles = []
    items = generate_vector()
    for i in range(int(No_Items)):
        for x in range(int(No_Items)):
            if i != x:
                angles.append(calc_angle(items[i], items[x]))
    avrg_angle = round(np.mean(angles), 2)
    return avrg_angle

def angles(a, b):
    vectors = generate_vector()
    angles = []
    if a != '':
        for i in range(1, int(No_Items) + 1):
            if str(i) not in b:
                angles.append([i,(calc_angle(vectors[(int(a) - 1)], vectors[(i - 1)]))])
    return sorted(angles,key=lambda x: x[1])[0]

def entries():
    vectors = generate_vector()
    count = 0
    for i in range(len(vectors)):
        for x in vectors[i]:
            if x == 1:
                count += 1
            else:
                count += 0
    return count

def item_recommend(z):
    order = sorted(z, key=lambda x: x[0])
    recommend_output = ""
    for i in order:
        recommend_output += ' ' + str(i[1]) + ' '
    return recommend_output

vectors = generate_vector()
cart_list = read_cart()
pos_entries = entries()
avrg_angle = average_angle()
print("Positive entries: " + str(pos_entries))

#average angle printed out
print("Average angle: " + str(avrg_angle))

#for loop which calculates the item
for i in cart_list:
    print("Shopping cart: " + i)
    recommend = []
    #order matches into a found_updated list
    found_updated = []
    cart_items = list(i.split(' '))
    for x in cart_items:
        match, angle = angles(x, i)
        if angle > 90:
            continue
        elif match not in found_updated:
            recommend.append([angle, match])
            found_updated.append(match)
        if angle < 90:
            print("Item: " + str(x) + " Match: " + str(match) + ", Angle: " + str(angle))
        else:
            print("Item: " + str(x) + " No match found!")
    print("Recommend: " + item_recommend(recommend))
