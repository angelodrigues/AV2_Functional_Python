import psycopg2

# Função para estabelecer a conexão com o banco de dados
connectToDb = lambda: psycopg2.connect(
    host="localhost",
    user="root",
    password="root",
    database="AV2"
)

# Função para criar a cláusula INNER JOIN
createInnerJoin = lambda table1, table2, col1, col2: (
    f"INNER JOIN {table2} ON {table1}.{col1} = {table2}.{col2}",
)

# Função para criar a cláusula SELECT
createSelect = lambda cols: (
    f"SELECT {', '.join(cols)}",
)

# Função para construir a consulta SQL completa
buildQuery = lambda selectStmt, joinStmts: (
    f"{selectStmt[0]} FROM GAMES {' '.join(joinStmts)}"
)

# Construindo as cláusulas INNER JOIN
joinStmt1 = createInnerJoin('GAMES', 'VIDEOGAMES', 'id_console', 'id_console')
joinStmt2 = createInnerJoin('VIDEOGAMES', 'COMPANY', 'id_company', 'id_company')

# Construindo a cláusula SELECT
selectStmt = createSelect(['GAMES.title', 'GAMES.release_date', 'COMPANY.name', 'VIDEOGAMES.name'])

# Construindo a consulta SQL completa
query = buildQuery(selectStmt, [joinStmt1[0], joinStmt2[0]])

# Executando a consulta e imprimindo os resultados
try:
    conn = connectToDb()
    cur = conn.cursor()
    cur.execute(query)
    results = cur.fetchall()
    print(results)

    for result in results:
        print(result)

    cur.close()
    conn.close()
except psycopg2.Error as e:
    print(f"Erro ao conectar ao banco de dados: {e}")
