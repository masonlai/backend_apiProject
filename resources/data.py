from flask_restful import Resource, request
from ..schema.data_schema import getSchema, customerSchema, Schema, checkSchema, updateSchema

bill = []
product = [
    {"orderItemCode": "1243", "description": "1234", "pricePerItem": 2},
    {"orderItemCode": "0002", "description": "potato chip", "pricePerItem": 10},
    {"orderItemCode": "0003", "description": "apple", "pricePerItem": 1}
]

getschema = getSchema(many=False)
customerschema = customerSchema(many=False)
schema = Schema(many=False)
checkschema = checkSchema(many=False)
updateschema = updateSchema(many=False)


class Data(Resource):

    def get_param(self):

        data = request.get_json(force=False)
        if data is None:
            data = request.form
        return data

    def checkproduct(self, productCode):

        global product
        price = ""
        for item in product:
            if item["orderItemCode"] == productCode:
                price = item["pricePerItem"]
        return price

    def post(self):
        result = schema.load(self.get_param())
        global bill
        pricePerItem = float(self.checkproduct(result["orderItemCode"]))
        totalPrice = ""
        if pricePerItem != "":
            totalPrice = pricePerItem * int(result["quantity"])
        else:
            return {
                       "message": "order item code not exist!"
                   }, 404
        try:
            data = {
                "orderNo": str(len(bill)),
                "orderItemCode": result["orderItemCode"],
                "description": result["description"],
                "quantity": result["quantity"],
                "pricePerItem": pricePerItem,
                "totalPrice": totalPrice,
                "customer": result["customer"],
                "address": result["address"],
                "date": result["date"],
                "time": result["time"]
            }
            bill.append(data)
            return {
                "message": "Insert data success",
                "data": checkschema.dump(data)
            }
        except:
            return {
                "message": "Insert data error",
                "data": checkschema.dump(data)
            }


class customerData(Resource):

    def get_param(self):

        data = request.get_json(force=False)
        if data is None:
            data = request.form
        return data

    def post(self):

        data = {}
        result = customerschema.load(self.get_param())

        i = 0

        for e in bill:
            if e['customer'] == result['customer']:
                data[i] = checkschema.dump(e)
                i = i + 1

        return {
            "data": data
        }


class getData(Resource):

    def get_param(self):

        data = request.get_json(force=False)
        if data is None:
            data = request.form
        return data

    def checkproduct(self, productCode):

        global product
        price = ""
        for item in product:
            if item["orderItemCode"] == productCode:
                price = item["pricePerItem"]
        return price

    def get(self):

        data = {}

        i = 0

        for e in bill:
            data[i] = checkschema.dump(e)
            i = i + 1

        return {
            "data": data
        }

    def post(self):

        result = getschema.load(self.get_param())
        find = [item for item in bill if item["orderNo"] == result["orderNo"]]

        if len(find) == 0:
            return {
                       "message": "orderNo not exist!"
                   }, 403
        else:
            data = find[0]
            return {
                "message": "",
                "data": checkschema.dump(data)
            }

    def put(self):

        result = updateschema.load(self.get_param())
        global bill
        find = None
        for item in bill:
            if item["orderNo"] == result["orderNo"]:
                find = item

                pricePerItem = float(self.checkproduct(result["orderItemCode"]))
                totalPrice = ""
                if pricePerItem != "":
                    totalPrice = pricePerItem * int(result["quantity"])

                item["orderItemCode"] = result["orderItemCode"]
                item["description"] = result["description"]
                item["quantity"] = result["quantity"]
                item["totalPrice"] = totalPrice
                item["customer"] = result["customer"]
                item["address"] = result["address"]

                return {
                    'message': 'Update order success',
                    'data': checkschema.dump(item)
                }

        if find == None:
            return {
                       'message': 'order not exist!'
                   }, 403

    def delete(self):

        result = getschema.load(self.get_param())
        global bill
        find = [item for item in bill if item["orderNo"] == result["orderNo"]]
        if len(find) != 0:
            bill.remove(find[0])
        return {
            'message': 'Delete done!'
        }



