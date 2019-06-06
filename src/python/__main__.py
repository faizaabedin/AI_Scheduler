import app
from pprint import pprint
from bson.objectid import ObjectId

# Connected database collection
#db = app.mongo.db
db = app.init_db()


def main():
    run_app = True
    print('''Greetings
    This is just for testing DB management operations''')
    menu = """
        Choose a command
        1 - Insert a new DB document
        2 - Remove a DB document
        3 - Update a DB document
        4 - Find document
        5 - Display all DB records
        0 - Exit/Return
    """

    print('Running...')

    while run_app:
        print(menu)
        selection = input()
        if selection == '1':
            insert_document()
        elif selection == '2':
            remove_document()
        elif selection == '3':
            update_document()
        elif selection == '4':
            find_document()
        elif selection == '5':
            display_documents()
        elif selection == '0':
            run_app = False
            print('byee')
        else:
            print('Invalid selection, please select a valid option')


def insert_document():
    name = input('Enter unique name: ')
   
    if name == '0': # return option
        return

    # check if document already exists
    existing = db.test.find_one({'name': name}) # find_one returns None if queried document is not available
    if existing is not None:
        print('Document already exists. Enter a new document name.')
        insert_document()

    # document name is unique, insert
    value = input('Enter value: ')
    entry_id = db.test.insert_one({
        'name' : name,
        'value' : value
    })

    print('Added: ', db.test.find({'name': name})[0])
    
    

def remove_document():
    name = input('Enter name: ')

    if name == '0': # return option
        return
    
    doc = db.test.find_one({'name': name})

    if doc is None:
        print('Document not available. Please enter a valid name.')
        remove_document()
    else:
        db.test.delete_one({'_id': ObjectId(doc['_id'])})
        print('Document deleted.')
        return


def update_document():
    name = input('Enter name of document to update: ')

    if name == '0': # return option
        return

    doc = db.test.find_one({'name': name})
    # check if document is available
    if doc is None:
        print('Document not available. Please enter a valid name.')
        remove_document()
    else:
        attribute = input('Enter attribute name to update: ')
        value = input('Enter ' + attribute + ': ')
        db.test.update_one({'name' : name}, {"$set": {attribute: value} })
        print('Updated: ')
        print(db.test.find_one({'name': name}))



def find_document():
    name = input('Enter name: ')

    if name == '0': # return option
        return

    doc = db.test.find_one({'name': name})
    # check if document is available
    if doc is None:
        print('Document not available. Please enter a valid name.')
        find_document()
    else:
        print('Document found: ')
        print(doc)
    


def display_documents():
    documents = db.test.find()

    # check if collection is empty
    if db.test.count() == 0:
        print('No documents found in current collection.')
        return 

    for doc in documents:
        print(doc)

    

if __name__ == '__main__':
    main()