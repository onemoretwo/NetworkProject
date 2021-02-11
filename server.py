from socket import *
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd

HOST = '127.0.0.1'   # or 127.0.0.1 or localhost
PORT = 20300
ADDR = (HOST,PORT)
BUFFER = 4096

#create a socket (SRV)
#see python docs for socket for more info

srv = socket(AF_INET,SOCK_STREAM)

#bind socket to address
srv.bind((ADDR))	#double parens create a tuple with one object
srv.listen(1) # maximum queued connections is 1
print("Server is ready")

#model
df = pd.read_csv('diabetes.csv')
X = df.drop("Outcome",axis=1).values
y = df['Outcome'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.80, random_state=1, stratify=y)
knn = KNeighborsClassifier(n_neighbors = 8)
knn.fit(X_train,y_train)
x = [[7, 196, 90, 0, 0, 39.8, 0.451 ,41]]
def test_predict(test_data):
    result = knn.predict(test_data)
    return result
print(test_predict(x))

while True:
    conn,addr = srv.accept() #accepts the connection
    print('...connected by', addr)
     
    height = conn.recv(BUFFER).decode()
    height = int(height) + 1
    conn.send(str(height).encode())

    conn.close()