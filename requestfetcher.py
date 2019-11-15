import mysql.connector
import dbconfig as cfg

class RequestFetcher:

    db = mysql.connector.connect(
        host=cfg.mysql['host'],
        user=cfg.mysql['user'],
        passwd=cfg.mysql['passwd'],
        database=cfg.mysql['database']
    )

    def get_req(self):
        curs = self.db.cursor()
        curs.execute("SELECT u.name "
                    "  FROM users u "
                    "  JOIN requests r "
                    "    ON u.userid = r.userid")
        return curs.fetchone()

    def clear_req(self):
        curs = self.db.cursor()
        curs.execute("DELETE FROM requests")

