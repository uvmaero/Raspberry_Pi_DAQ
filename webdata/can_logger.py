# Log relevent CAN data to sql database

import mysql.connector
import json
import datetime
import time
import can

# create CAN interface
can.rc['interface'] = 'socketcan'
can.rc['channel'] = 'vcan0' # vcan0 for virtual, can0 for live
can.rc['bitrate'] = 500000
bus = can.interface.Bus()

can_ID = 0x0C0

def get_can_message(id):
    for message in bus:
        if message.arbitration_id == id:
            data = message.data[0]
            return data

def store_data(canID):
    #load database credentials
    credentials = json.load(open("credentials.json", "r"))

    #connect to database
    database = mysql.connector.connect(
            host=credentials["host"],
            user=credentials["user"],
            passwd=credentials["password"],
            database=credentials["database"]
            )

    # create cursor to execute database commands
    cursor = database.cursor()

    # sql insert statement
    insert_sql = "INSERT INTO `can_data` (`timestamp`, `canID`, `msg`) VALUES (%s,%s,%s);"

    # get time
    now = datetime.datetime.now()

    # get CAN message
    msg = get_can_message(canID)

    # print to display
    print(msg)

    # insert into database
    data = (now,canID, msg)
    cursor.execute(insert_sql,data)

    # commit inser to databse
    database.commit()

    # close database connection
    cursor.close()
    database.close()

    # sleep
    #time.sleep(0.25)

#while True:
#    store_data(can_ID)
    
