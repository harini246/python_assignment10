import os
file = 'example.txt'
location = 'C:\\Users\\sai alekhya\\Documents'
path = os.path.join(location, file)
os.remove(path)
