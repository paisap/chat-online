from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.irish
prueba = db.pruebaColection
post_data = {
    'title': 'Python and MongoDB',
    'content': 'PyMongo is fun, you guys',
    'author': 'Scott'
}
result = prueba.insert_one(post_data)
print('One post: {0}'.format(result.inserted_id))