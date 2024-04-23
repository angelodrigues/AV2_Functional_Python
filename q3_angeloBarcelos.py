import psycopg2

class Database:
    def __init__(self, conn_params):
        self.conn_params = conn_params
        self.conn = None

    connect = lambda self: self.conn if hasattr(self, 'conn') and self.conn is not None else (
        print("Conectando ao banco de dados...") or setattr(self, 'conn', psycopg2.connect(**self.conn_params)) or self.conn if hasattr(self, 'conn_params') else print("Erro: atributo 'conn_params' não encontrado.")
    )

    disconnect = lambda self: self.conn.close() if self.conn else None

    def execute(self, query, args=None):
        connect_if_needed = lambda: self.connect() if not self.conn else None
        connect_if_needed()
        cursor = lambda: self.conn.cursor()
        cursor = cursor()
        cursor.execute(query, args)
        return cursor

    insert = lambda self, table, fields, values: (lambda query, values: (self.execute(query, values), self.conn.commit()))(f"INSERT INTO {table} ({', '.join(fields)}) VALUES ({', '.join(['%s'] * len(values))})", values)

    get_all = lambda self, table: (lambda query: self.execute(query).fetchall())(f"SELECT * FROM {table}")

    get_by_id = lambda self, table, id: (lambda query, id: self.execute(query, (id,)).fetchone())(f"SELECT * FROM {table} WHERE id = %s", id)

    update = lambda self, table, id, fields, values: (lambda query, id, values: (self.execute(query, (*values, id)), self.conn.commit()))(f"UPDATE {table} SET {', '.join([f'{field}=%s' for field in fields])} WHERE id = %s", id, values)

    delete = lambda self, table, id: (lambda query, id: (self.execute(query, (id,)), self.conn.commit()))(f"DELETE FROM {table} WHERE id = %s", id)

try:
    conn_params = lambda host, dbname, user, password: {
        "host": host,
        "dbname": dbname,
        "user": user,
        "password": password
    }

    db = lambda: Database(conn_params("localhost", "AV2", "root", "root"))
    db = db()

    db.insert("USERS", ["id", "name", "country", "id_console"], [4, "Angelo Rodrigues", "Brasil", 4])
    print(db.get_all("USERS"))
    print(db.get_by_id("USERS", 1))

    db.update("USERS", 1, ["name"], ["Angelo Barcelos"])
    print(db.get_by_id("USERS", 1))

    db.delete("USERS", 1)
    print(db.get_all("USERS"))

except Exception as e:
    print(f"Erro geral: {e}")

finally:
    db.disconnect()
