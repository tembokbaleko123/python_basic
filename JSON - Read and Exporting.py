#Read JSON Data
import json
 
 
Dictionary ={'Halo':123,'Semua':456}
 
json_string = json.dumps(Dictionary)
 
print('Result: ',json_string)
print('Tipe: ',type(json_string))

#Exporting JSON data
#json.dump().