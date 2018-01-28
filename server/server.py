import SqlDb as db
import config as cfg
import socket
import pickle
from threading import Thread, Lock

mutex = Lock()


def looking_for_update():
    """ Look for update each DELTA_TIME sec for each user of the DB"""
    return


def add_user(dict_user):
    """ Add user in DB """
    mutex.acquire()
    try:
        toto = "toto"  # TODO: unpickle data + send cmd to DB
    finally:
        mutex.release()

    return True


def main():
    """ Server of IsMyTweet << Should be running on the same host than the server """
    """ 1) Wait for user input to update database << Open socket for Flask app 
        2) Check for each user if change in nb of twitter 
        3) If change, run checker twitter << use deep learning / nlp fct on message scrapped 
        TODO : 
            - message scrapped saved in DB ?
    """
    try:
        # Open DB File
        sql_db = db.SqlDb(cfg.DB_FILE_NAME)
        if not sql_db:
            print("Impossible to open db file")

        # Open thread

        # Open socket
        server_socket = socket.socket()
        server_socket.bind(cfg.SOCKET_SERVER)
        server_socket.listen(cfg.NB_SIMUL_CONNECTION)

        # Wait for command from App Web to update database
        exit_cmd = False
        while not exit_cmd:
            (client_socket, client_address) = server_socket.accept()
            client_cmd = client_socket.recv(cfg.DATA_SIZE_MAX)
            print("rec : " + str(client_cmd))
            #data_loaded = pickle.load(client_cmd)
            #is_user_added = add_user(data_loaded)
            #if not is_user_added:
            client_socket.send("Existing user".encode())  # TODO: should send ID instead

    except socket.error as err:
        print('Socket : impossible to open. ErrorCode : ' + err)

    finally:
        client_socket.close()
        server_socket.close()

        if sql_db:
            sql_db.close_table()


if __name__ == "__main__":
    main()
