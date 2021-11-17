import db

def create(table, object):    
    object["id"] = len(table)
    table.append(object)

def read(table, id):
    for elm in table:
        if elm["id"] == id:
            return elm

    return "Not Found"

def update(table, id, object):
    for elm in table:
        if elm["id"] == id:

            for key, value in object.items():
                elm[key] = value
            
            return elm

    return "Not Found"

def delete(table, id):
    for index in range(len(table)):
        if table[index]["id"] == id:
            table.pop(index)
            return 

    return "Not Found"
