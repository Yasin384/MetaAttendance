import firebase_admin
from firebase_admin import credentials, db

# Загрузите ключ учетной записи сервиса (serviceAccountKey.json)
cred = credentials.Certificate('path/to/serviceAccountKey.json')

# Инициализация приложения
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://meta-educate-default-rtdb.firebaseio.com'
})

def get_database():
    return db.reference()
