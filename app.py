# Create your own db.py with mongodb connection details, DO NOT commit that file
# PM me on telegram your connection string, username and password

from db import db

# Create
# neworder = {"orderID": "order1234", "amount": 12.34, "userID": "user123", "shopID": "shop1234", "status": "false"}
# db.Orders.insert_one(neworder)

# Read
# sortedOrders = list(db.Orders.find({}, {"_id": 0}).sort("amount", -1))
# orderLen = len(sortedOrders)
# if orderLen <= 6:
#     response = sortedOrders
#     print(response)
# else:
#     response = []
#     for i in range(0, 6):
#         response.append(sortedOrders[i])
#         print(response)

# Update
# filter_con = {"status": "false"}
# update_con = {"$set": {"status": "Dispute"}}
# db.Orders.update_many(filter_con, update_con)

# Delete
# db.Orders.delete_many({"orderID": "order789"})
