import json

def read_json_file(file_path):
  with open(file_path,'r') as f:
    data=json.load(f)
  return data

def get_value(data, key):
  return data.get(key,None)

def write_value(dat,file_path):
  with open(file_path,'w') as f:
    json.dump(data,f,indent=4)
  
