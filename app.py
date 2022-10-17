# Create your own db.py with mongodb connection details, DO NOT commit that file
# PM me on telegram your connection string, username and password

from typing import List
from venv import create

from bson import ObjectId
from db import db
import test

# Create

# Create new user 
# returnResult = db.users.insert_one(
#     {
#         "name": test.purchasing_user, 
#         "age": 19,
#         "address": ""
#     })

# Create new order 
def create_new_order(data): 
    return_result = db.orders.insert_one(data)
# test_data =  {
#             "amount" : float(10),
#             "userID": test.user_id, 
#             "shopID": test.shop_id,
#             "status": "Completed"
#         }
# create_new_order(test_data); 

# Read
def get_transactions(): 
    # Return all orders in the db (won't work if db is huge)
    top_ten_orders = db.orders.find({}).sort("amount", -1).limit(10)
    filtered_orders = top_ten_orders[4: 10]
    # for object in filtered_orders:
    #     print(object['amount'])
    return filtered_orders

# get_transactions()

# Update

# Delete
def delete_corresponding_orders(id): 
    returnResult = db.orders.delete_many({"_id": id})

delete_corresponding_orders(test.order_id)
#
