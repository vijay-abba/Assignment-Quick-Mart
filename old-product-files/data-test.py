
from pathlib import Path
import json

file_path = Path("data")
file_name = file_path / f"products.txt"

# WRITING 
products = []

def add_to_List(id, name, quantity):
    new_obj = {
        "id": id,
        "name": name,
        "quantity": quantity
    }
    products.append(new_obj)



""" Write """
# creating to json string 
user_list_json = json.dumps(products)

with open(file_name, "w") as f:
    f.write(user_list_json)


# LISTENING
print("reading ---")

with open(file_name, "r") as f:

    obj = f.readline()
    print(type(obj))
    # converting to list
    product_list = json.loads(obj)
    print(product_list)
    print(type(product_list))

    for i in product_list:
        print(i)

