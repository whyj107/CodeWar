# Simple Socket Client
# https://www.codewars.com/kata/639107e0df52b9cb82720575/train/python

# 풀이
import socket
def socket_client():
    truth = b'Hello World'
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as ws:
        ws.connect(("127.0.0.1", 1111))
        ws.sendall(truth)
        response = ws.recv(1024)
        return response==truth
