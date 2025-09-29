import sqlite3
from modules.log_class import logger

class DbClass():
    def __init__(self, parent = None):
        super().__init__()

        #variable setup
        self.conn = sqlite3.connect("jhmr.db")
        self.cur = self.conn.cursor()
        
        self.initialize_database()
        
    #add returning to every query
    def execute_single_query(self,q=None,values=None):
        if q[len(q) - 1] != ";":
            logger.error(f"Não esqueça do ; na query: {q}")
            return
        res = ''
        try:
            if q and values:
                print(q,values)
                self.cur.execute(q,values)
            elif q and values == None:
                self.cur.execute(q)
            else:
                logger.error(f"Query: {q}\nValores: {q}")
                return
            res = self.cur.fetchall()
            self.conn.commit()
            if self.cur.rowcount == 0:
                return None
            else:
                return res
        except Exception as e:
            logger.error(f"Erro ao tentar executar a seguinte query: \n{q}\nErro: {e}")
            
    def execute_multiple_queries(self,q=None,values_array=None):
        if q[len(q) - 1] != ";":
            logger.error(f"Não esqueça do ; na query: {q}")
            return
        res = ''
        try:
            if q and values_array:
                self.cur.executemany(q,values_array)
                res = self.cur.fetchall()
                self.conn.commit()
                if self.cur.rowcount == 0:
                    return None
                else:
                    return res
            else:
                logger.error(f"Query: {q}\nValores: {q}")
        except Exception as e:
            logger.error(f"Erro ao tentar executar a seguinte query: \n{q}\nErro: {e}")
             
    def initialize_database(self):
        self.execute_single_query("""
            create table if not exists therapist (
                id INTEGER primary key,
                name text not null,
                details text not null,
                image_path text,
                created_at timestamp default current_timestamp
            );""")
        self.execute_single_query("""
            create table if not exists patient(
                id integer primary key,
                name TEXT NOT NULL,
                details TEXT NOT NULL,
                image_path TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );""")
        self.execute_single_query("""
            create TABLE use_statistics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER NOT NULL,
            session TIMESTAMP NOT NULL default current_timestamp,
            index_counter INTEGER,
            middle_counter INTEGER,
            ring_counter INTEGER,
            little_counter INTEGER,
            thumb_counter INTEGER,
            average_pressure INTEGER,
            max_pressure INTEGER,
            average_time INTEGER,
            FOREIGN KEY (patient_id) REFERENCES patient(id)
            );""")