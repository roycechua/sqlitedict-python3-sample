from sqlitedict import *

mydict = SqliteDict("some.db", autocommit=True)
mydict["accounts"]=[{"id":1,"name":"John Doe"},{"id":2,"name":"Edward Snowden"}]

def search(id):
    """ Search for an account using the id
        search(id) # id is an integer
        The output prints the account name associated with the id
    Example: 
        search(2)
    """
    for account in mydict["accounts"]:
        if account["id"]==id:
            print(account["name"])
            
def main():
    id = int(input("Enter an id: "))
    search(id)

if __name__ == "__main__":
    main()