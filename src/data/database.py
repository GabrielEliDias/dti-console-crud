import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent.parent
DB_PATH = ROOT_DIR / 'src' / 'data' / 'db_livros.db'
SCRIPT_PATH = ROOT_DIR / 'sql' / 'init_db.sql' 

def inicializar_banco():
    conn = None

    if not SCRIPT_PATH.exists():
        print(f"Erro: Arquivo de script não encontrado em {SCRIPT_PATH}")
        return
    try:
        conn = sqlite3.connect(DB_PATH)

        with open (SCRIPT_PATH, 'r', encoding="utf-8") as f:
            script_comandos = f.read()  

        cursor = conn.cursor()
        cursor.executescript(script_comandos)

        print("Banco de dados verificado/inicializado corretamente!")
    except sqlite3.Error as e:
        print(f"Erro ao inicializar o banco de dados: {e}")

    finally:
        if conn:
            conn.close()

def get_conexao():
    return sqlite3.connect(DB_PATH)