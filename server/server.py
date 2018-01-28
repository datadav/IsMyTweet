import SqlDb as db
import config as cfg
import socket
import pickle
import time
from model_ml import ProcUnit as pu
from threading import Thread, Lock

mutex = Lock()


def looking_for_update():
    """
    Thread target
    Look for update each DELTA_TIME sec for each user of the DB
    1) get mutex for each read in DB
    2) look in DB for next user
    3) run model on current user
    4) send notification when needed
    """
    while True:  # No delta time for now
        mutex.acquire()
        try:
            # pu_obj = pu.ProcUnit()
        finally:
            mutex.release()
            time.sleep(cfg.DELTA_TIME)
    return


def add_user(sql_db, dict_user):
    """ Add user in DB """
    mutex.acquire()
    try:
        if not sql_db.is_in_table(name_twitter):
            sql_db.insert_in_table(name_twitter, email, avatar)
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
        t = Thread(target=looking_for_update)
        t.start()

        # Open socket
        server_socket = socket.socket()
        server_socket.bind(cfg.SOCKET_SERVER)
        server_socket.listen(cfg.NB_SIMUL_CONNECTION)

        # Wait for command from App Web to update database
        exit_cmd = False
        while not exit_cmd:
            (client_socket, client_address) = server_socket.accept()

            client_cmd = client_socket.recv(cfg.DATA_SIZE_MAX)
            data_loaded = pickle.load(client_cmd)

            id_user = add_user(sql_db, data_loaded)
            client_socket.send(str(id_user).encode())

    except socket.error as err:
        print('Socket : impossible to open. ErrorCode : ' + err)

    finally:
        client_socket.close()
        server_socket.close()

        if sql_db:
            sql_db.close_table()


if __name__ == "__main__":
    main()
