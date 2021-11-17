import db

def create(collection, object):    
    object["id"] = len(collection)
    collection.append(object)

def read(collection, id):
    for elm in collection:
        if elm["id"] == id:
            return elm

    return "Not Found"

def update(collection, id, object):
    for elm in collection:
        if elm["id"] == id:

            for key, value in object.items():
                elm[key] = value
            
            return elm

    return "Not Found"

def delete(collection, id):
    for index in range(len(collection)):
        if collection[index]["id"] == id:
            collection.pop(index)
            return 

    return "Not Found"