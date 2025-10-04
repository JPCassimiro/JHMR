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
                id integer primary key,
                name text not null,
                details text not null,
                image_path text
            );""")
        self.execute_single_query("""
            create table if not exists patient(
                id integer primary key,
                name text not null,
                details text not null,
                image_path text
            );""")
        self.execute_single_query("""
            create table if not exists session (
                id integer primary key,
                patient_id integer not null,
                session_date timestamp not null default current_timestamp,
                foreign key (patient_id) references patient(id) on delete cascade
            );""")
        self.execute_single_query("""
            create table if not exists use_data (
                id integer primary key,
                session_id integer not null,
                finger text check(finger in ('index','middle','ring','little')),
                pressure integer not null,
                timestamp datetime default current_timestamp,
                foreign key (session_id) references session(id) on delete cascade
            );""")
        self.execute_single_query("""insert into patient (id, name, details, image_path)
            values (1, 'paciente padrão', 'valor padrão', '_internal/resources/imgs/placeholder_profile.png');""")
        self.execute_single_query("""insert into therapist (id, name, details, image_path)
            values (1, 'terapeuta padrão', 'valor padrão', '_internal/resources/imgs/placeholder_profile.png');""")