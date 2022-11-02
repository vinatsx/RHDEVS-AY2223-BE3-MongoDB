# Create your own db.py with mongodb connection details, DO NOT commit that file
# PM me on telegram your connection string, username and password

import datetime

from db import db

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
    db.orders.insert_one(data)
# test_data =  {
#             "amount" : float(10),
#             "userID": test.user_id, 
#             "shopID": test.shop_id,
#             "status": "Completed"
#         }
# create_new_order(test_data); 

# Read
def get_transactions(): 
    # Return all orders in the db
    top_ten_orders = db.orders.find({}).sort("amount", -1).limit(10)
    filtered_orders = top_ten_orders[4: 10]
    # for object in filtered_orders:
    #     print(object['amount'])
    return filtered_orders

# get_transactions()

# Update
def updateOrders(date):
    req_date = datetime.strptime(date, '%d-%m-%y') 
    length = db.orders.count_documents({})
    all_orders = db.orders.find()
    for i in range(0, length):
        if all_orders[i]['date'] > req_date:
            db.orders.update_one({"_id": all_orders[i]['_id']}, { "$set": { 'status': "Dispute"}})

# Delete
def delete_corresponding_orders(id): 
    db.orders.delete_many({"_id": id})

# delete_corresponding_orders(test.order_id)
#
