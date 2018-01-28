import sqlite3 as lite
import datetime

class SqlDb(object):
    """
    Class to manage SQLITE db
    """
    db_handler = None

    def __init__(self, db_table):
        """ Constructor """
        self.db_handler = lite.connect(db_table)

    def create_table(self, db_schema_table):
        """ Create Table or Open it if exists"""

        with self.db_handler:
            # Open and read the file as a single buffer
            fd = open(db_schema_table, 'r')
            sqlFile = fd.read()
            fd.close()

            # all SQL commands (split on ';')
            sqlCommands = sqlFile.split(';')

            # Execute every command from the input file
            for command in sqlCommands:
                try:
                    self.db_handler.execute(command)
                except ValueError as msg:
                    return False

        return True

    def is_in_table(self, name_twitter):
        """
        Check if this ID is already registered
        :param id_twitter:
        :return:
        """
        count_cmd = "SELECT COUNT(*) FROM users WHERE Name_Twitter = %s;" % name_twitter

        if self.execute(count_cmd) != 0:
            return True

        return False

    def insert_in_table(self, name_twitter, email, avatar):
        """
        Check if this ID is already registered
        :param name_twitter:
        :param email:
        :param avatar:
        :return:
        """
        ins_cmd = "INSERT INTO users VALUES (0, %s, %s, %s, 0, %s, 1);" % (name_twitter, avatar, email, datetime.datetime())

        if self.execute(ins_cmd) != 0:
            return True

        return False

    def execute_cmd(self, cmd):
        """ Execute command and get return value """
        try:
            cur = self.db_handler.cursor()
            cur.execute(cmd)
            data = cur.fetchone()

        except lite.Error as e:
            print("Error %s:" % e.args[0])

        return data

    def close_table(self):
        """ close handler """
        self.db_handler.close()
