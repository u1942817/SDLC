#CLASSES/TABLES IN DB
#Now that we want to use the database to save data, we can use the native pymongo to operate MongoDB, but here we need to simplify our operations, so we need to create data models.

#The main function of the data model is to show which fields our data contains, what type each field is, what is the attribute (unique, or one of several fixed values), and so on.This can help us to know the information of our data at all times when operating data, even if we don’t look at the data in the database.

#Here we are introducing the Flask extension of the MongoDB: MongoEngine. You can use MongoEngine independently without relying on the Flask, but you can use it in combination with Flask.

#To use MongoEngine in Flask, first we need to configure MongoDB’s information in Flask before we initialize the MongoEngine with our server, so that we connect the database and the server, which can be said in code:

#USER TABLE
class User(db.Document):
    name = db.StringField()
    email = db.StringField()
