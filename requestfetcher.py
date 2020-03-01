import mysql.connector
import dbconfig as cfg

class RequestFetcher:

    db = mysql.connector.connect(
        host=cfg.mysql['host'],
        user=cfg.mysql['user'],
        passwd=cfg.mysql['passwd'],
        database=cfg.mysql['database']
    )
    db.start_transaction(isolation_level='READ COMMITTED')
    
    def get_req(self):
        curs = self.db.cursor()
        curs.execute("SELECT u.name FROM users u "\
                     "JOIN requests r ON u.userid = r.userid "\
                     "WHERE current_timestamp < date_add(date, INTERVAL 2 MINUTE);")
        ret_list = []
        records = curs.fetchall()
        for row in records:
            ret_list.append(row[0])

        curs.close()
        return ret_list

    def clear_req(self):
        curs = self.db.cursor()
        curs.execute("DELETE FROM requests")

