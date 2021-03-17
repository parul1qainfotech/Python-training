import requests
import json

# URL='http://127.0.0.1:8000/stu/'
# URL='http://127.0.0.1:8000/stucreate/'
URL='http://127.0.0.1:8000/sturead/'
# URL='http://127.0.0.1:8000/stuupdate/'

# r=requests.get(url=URL)
# print(r.json())


#for deserialization
# for create
# data={
#     'name':'reeta',
#     'roll':12,
#     'city':'mohali'
# }

# json_data= json.dumps(data)
# r=requests.post(data=json_data,url=URL)
# data=r.json()
# print(data)


# for read

def get_data(id= None):
    if id is not None:
        data={'id':id}
        json_data=json.dumps(data)
        r=requests.get(data=json_data,url=URL)
        print(r.json())
        
        
get_data(3)


# def update_data():
#     data={
#     'id':4,
#     'name':'monika',
#     'city':' mumbai'}
#     json_data=json.dumps(data)
#     r=requests.put(data=json_data,url=URL)
#     print(r.json())
        
# update_data()


