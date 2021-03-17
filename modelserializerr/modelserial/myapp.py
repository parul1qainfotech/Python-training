import requests
import json
URL='http://127.0.0.1:8000/all_method_class/'

headers={'content-Type':'application/json'}
def get_data(id= None):
    if id is not None:
        data={'id':id}
        json_data=json.dumps(data)
        r=requests.get(data=json_data,url=URL,header=headers)
        print(r.json())

        
get_data()

headers={'content-Type':'application/json'}

def post():
    data={
        'id':5,
        'name':'geeta',
        'roll':44,
        'city':'noida'
    }
    json_data=json.dump(data)
    r=requests.post(data=json_data,url=URL,header=headers)
    print(r.json())

# post()

headers={'content-Type':'application/json'}

def update_data():
    data={
    'id':4,
    'name':'monika',
    'city':' mumbai'}
    json_data=json.dumps(data)
    r=requests.put(data=json_data,url=URL,header=headers)
    print(r.json())
        
# update_data()  
    
headers={'content-Type':'application/json'}
def delete(id):
    r=requests.put(data=id,url=URL,header=headers)
    print(r.json())
    
# delete()