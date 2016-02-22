import datetime

now = datetime.datetime.now()
format = '%Y-%m-%d %H:%M:%S'
print now.strftime(format)

conn = MySQLdb.connect(host=localhost, user=root, passwd=whobutJ90, db=flight_data)

query = "INSERT INTO flight_table (planeID,ADSHEX,longitude,latitude,altitude,radarID,aircraft,departing,destination,dateTime) VALUES "

for planeID in theJSON:
        if '8' in planeID:
#        							planeID 				ADSHEX 						long 							lat 					alt 						radar 						aircraft 						from 							to
            query = query + "'(" + planeID + "','" + theJSON[planeID][0] + "'," + theJSON[planeID][1] + "," + theJSON[planeID][2] + "," + theJSON[planeID][4] + ",'" + theJSON[planeID][7] + "','" + theJSON[planeID][8]  + "','" + theJSON[planeID][11] + "','" + theJSON[planeID][12] + "'," + now  + ")," 
# replace final comma with semi-colon
if query.endswith(','):
    query = query[:-1]
    query = query + ';' 

            , "ADSHEX: ", theJSON[planeID][0], "longitude: ", theJSON[planeID][1], "latitude: ", theJSON[planeID][2], 
                "altitude: ", theJSON[planeID][4], "radarID: ", theJSON[planeID][7],"Aircraft: ", theJSON[planeID][8], "Reg No.", theJSON[planeID][9], 
                "From: ", theJSON[planeID][11], "To: ", theJSON[planeID][12])