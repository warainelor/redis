import redis

# connect to redis
client = redis.StrictRedis(host='localhost', port=60782, db=0)

# check connection
try:
    client.ping()
    print("connection to redis is successful")
except redis.ConnectionError:
    print("connection to redis is failed")

# add values to redis
# set key value pair
client.set('name', 'Alice')

# get value by key
name = client.get('name')
print(f"value by key 'name': {name.decode('utf-8')}")

# delete key
client.delete('name')
print("key 'name' is deleted ")

# using list
# add items to list
for item in ['item1', 'item2', 'item3']:
    client.rpush('mylist', item)

# get item from list
items = client.lrange('mylist', 0, -1)
print("items in list 'mylist':", [item.decode('utf-8') for item in items])

# incrementing value by key (using int)
client.set('counter', 10)
client.incr('counter')
print(f"new value of counter: {client.get('counter').decode('utf-8')}")

# work with hash (dictionary)
client.hset('user:1000', 'name', 'John')
client.hset('user:1000', 'age', 30)

# get every value of dictionary
user = client.hgetall('user:1000')
print("userdata: ", {k.decode('utf-8'): v.decode('utf-8') for k, v in user.items()})