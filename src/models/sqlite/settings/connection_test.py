from .connection import db_connection_handler
from sqlalchemy.engine import Engine


def test_db_connection():

 assert db_connection_handler.get_db() is None #Verifica se a conexao é nula antes de chamar a a funcao para se conectar

 db_connection_handler.connect_to_db() # Chama a funcao que conecta ao banco de dados
 db_engine = db_connection_handler.get_db() # Cria uma variável para instanciar essa conexao

 assert db_engine is not None # Verifica que a conexao agora existe...
 assert isinstance(db_engine, Engine) #Assegura que é um conexao válida do Engine do sqlAlchemy
  