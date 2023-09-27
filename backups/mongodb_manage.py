import pymongo


class calibrationController:
    def mongodb_quick_save(self, connection_string, database, cluster, data):
        myclient = pymongo.MongoClient(connection_string)
        mydb = myclient[database]
        mycol = mydb[cluster]

        mydict = data

        x = mycol.insert_one(mydict)

        print(x)

    d = {"name": "John", "address": "Highway 37"}
    mongodb_quick_save("mongodb://192.99.144.77:27023/",
                       "test_database", "demo", d)
    print("Saved")
