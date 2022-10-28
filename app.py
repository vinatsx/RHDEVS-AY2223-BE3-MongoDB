import pymongo
from datetime import datetime 

DB_USERNAME = ""
DB_PASSWORD = ""
DB_LINK = ""

URL = DB_LINK.format(
    DB_USERNAME, DB_PASSWORD)

client = pymongo.MongoClient(URL)
db = client["TakeFood"]

#insert user purchase
def insertUserPurchase(details):   #details will be passed in JSON format
    order = {"orderID": details['orderID'],
            "amount": details['amount'], 
            "userID": details['userID'],    
            "shopID": details['shopID'], 
            "status": details['status']}
    db.Orders.insert_one(order)
    filter_con = {"userID": details['userID']}
    new_con = { "$push": { 'orders': details['orderID']}}
    db.Users.update_one(filter_con, new_con)

#sorry ass method (read)
def retrieveFifthtoTenth():
    def get_amount(order):
        return order.get('amount')
    orders = db.Orders.find()
    #length = db.Orders.count_documents({})
    order_list = []
    for order in orders:
        order_list.append(order)
    order_list.sort(key=get_amount)
    result = []
    for i in range(4, 10):
        result.append(order_list[-i])
        print(f"{i+1}th largest transaction: {order_list[-i]}")  #laze to present properly
    return result

#update
def orderDisputes(date):
    new_con = { "$set": { 'status': "Dispute"}}
    req_date = datetime.strptime(date, '%d-%m-%y') 
    length = db.Orders.count_documents({})
    orders = db.Orders.find()
    for i in range(0, length):
        if orders[i]['date'] > req_date:
            filter_con = {"orderID": orders[i]['orderID']}
            db.Orders.update_one(filter_con, new_con)

#delete
def deleteOrder(orderID):
    db.Orders.delete_one({'orderID': orderID})
