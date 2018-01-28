import config as cfg
import socket
import pickle


def main():
    i = 0
    while True:
        try:
            my_socket = socket.socket()
            my_socket.connect(cfg.SOCKET_SERVER)

            test_msg = {"test":"test n°+"+str(i)}
            i += 1
            data_sent = pickle.dumps(test_msg)
            my_socket.send(data_sent)

            data = my_socket.recv(255)

            print('The server sent : ' + data.decode())

        except socket.error as err:
            print('Server not found.')

        finally:
            my_socket.close()


if __name__ == "__main__":
    main()