from db import engine, Login_info, dbsession, session

query_uname = dbsession.query(Login_info.uname).filter(Login_info.uname == 'asd').one()
print(query_uname)
str1 = query_uname[0]
print(str1)
print(query_uname[(0)])