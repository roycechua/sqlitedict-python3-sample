from sqlitedict import *

# simple example of Sqlitedict
dictionarydb = SqliteDict("some.db", autocommit=True) # access the db
# make 2 new accounts
accounts_list = dictionarydb.get('accounts',[])
accounts_list.append({"id":1,"name":"John Doe"})
accounts_list.append({"id":2,"name":"Edward Snowden"})
dictionarydb["accounts"] = accounts_list
print("new dictionary database", dictionarydb["accounts"])

# make another new account
accounts_list = dictionarydb.get('accounts')
accounts_list.append({"id":3,"name":"Royce Chua"})
dictionarydb["accounts"] = accounts_list
print(dictionarydb["accounts"])

# modify values
accounts_list = dictionarydb.get('accounts')
accounts_list[2]["name"] = "Roycee Chuaa"
dictionarydb["accounts"] = accounts_list
print(dictionarydb["accounts"])

# delete record of edward snowden
accounts_list = dictionarydb.get('accounts')
accounts_list.pop(1)
dictionarydb["accounts"] = accounts_list
print(dictionarydb["accounts"])

dictionarydb.close() # add a close to free-up resources


