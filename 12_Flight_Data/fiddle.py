import datetime

now = datetime.datetime.now()
format = '%Y-%m-%d %H:%M:%S'
print now.strftime(format)

conn = MySQLdb.connect(host=localhost, user=root, passwd=whobutJ90, db=flight_data)

query = "INSERT INTO flight_table (planeID,ADSHEX,longitude,latitude,altitude,radarID,aircraft,departing,destination,dateTime) VALUES "

for planeID in theJSON:
        if '8' in planeID:
#        							planeID 				ADSHEX 						long 							lat 					alt 						radarID 						aircraft 						from 							to
            query = query + "'(" + planeID + "','" + theJSON[planeID][0] + "'," + theJSON[planeID][1] + "," + theJSON[planeID][2] + "," + theJSON[planeID][4] + ",'" + theJSON[planeID][7] + "','" + theJSON[planeID][8]  + "','" + theJSON[planeID][11] + "','" + theJSON[planeID][12] + "'," + now  + ")," 
# Replace final comma with semi-colon in the query
if query.endswith(','):
    query = query[:-1]
    query = query + ';' 


print 'Insert Query: ' + query
x = conn.cursor()
x.execute(query)
conn.commit()
row = x.fetchall()