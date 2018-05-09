import csv

def generate_keys():
    with open('API_Keys.csv','rt') as keyfile:
        c = csv.reader(keyfile)
        return {st : key for [st,key] in keyfile
        
api_keys = generate_keys()