import socket
import time
import pickle

HEADER_SIZE = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1236))
s.listen(5)

while True:
    client_socket, address = s.accept()
    print(f"connection from {address} has been established")

    test_dict = {"1": "Hey", "2": "There"}
    msg = pickle.dumps(test_dict)
    # print(msg)
    msg = bytes(f"{len(msg) :< {HEADER_SIZE}}", "utf-8") + msg

    client_socket.send(msg)
