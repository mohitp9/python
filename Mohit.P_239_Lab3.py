def decode(stringsplit):
    str=stringsplit.split('_')
    str=[str.strip() for str in str if str.strip()]
    dict={
        "Name":str[0],
        "Domain_name":str[1],
        "Regno":str[2]
    }
    return dict
encode="Mohit P__Traffic Control___2347239"
dict=decode(encode)
print(dict)