# Log relevent CAN data to sql database

import mysql.connector
import json
import datetime
import time
import can
import matplotlib
import matplotlib.pyplot
import matplotlib.animation as animation

# create CAN interface
can.rc['interface'] = 'socketcan'
can.rc['channel'] = 'can0' # vcan0 for virtual, can0 for live
can.rc['bitrate'] = 500000
bus = can.interface.Bus()

can_ID = 0x0C0

#get data from main.html java function (submitInfo)
#@app.route('/getmethod/<jsdata>')
#def get_javascript_data(jsdata):
#	return jsdata

# declare plot and axis data lists
# x1 = []
# y1 = []
# fig = plt.figure() #creates figure object
# ax = fig.add_subplot(1,1,1) #creates axis object in the figure
# ax.set_title("Plot 1", fontsize='large')

def get_can_message(id, bit):
    for message in bus:
        if message.arbitration_id == id:
            data = message.data[bit]
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

    # add to axis lists
    y1.append(msg)
    x1.append(now) #timestamp

    # insert into database
    data = (now,canID, msg)
    cursor.execute(insert_sql,data)

    # commit inser to databse
    database.commit()

    # close database connection
    cursor.close()
    database.close()

    # update graph
    graph(x1,y1)

    # sleep
    #time.sleep(0.25)

def graph(x1, y1):
   # draw the axis data:
   ax.clear()
   ax.plot(x1,y1)

   # format graph
   plt.xticks(rotation=45, ha='right')
   plt.subplots_adjust(bottom=0.30)
   plt.title('Test table')
   plt.xlabel('Time')
   plt.ylabel('CAN data')

# call for graph generation every second
#ani = animation.FuncAnimation(fig, store_data, fargs=(x1,y1), interval=1000)

#fig.show() --> generates an image of the graph, usually in GUI window
#save_html(plt, "templates/main.html") #save fig to main.html
