from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ....config.base import setings

def Create_Engine(database_password , database_username , database_connection_name , databese_host , database_port , database_name):
    return create_engine(f"{database_connection_name}://{database_username}:{database_password}@{databese_host}:{database_port}/{database_name}")

Session = sessionmaker(bind=Create_Engine(setings.DATABASE_PASSWORD , setings.DATABASE_USENAME , "postgresql" , setings.DATABASE_HOST , setings.DATABASE_PORT , setings.DATABASE_NAME))
sesion = Session()
# class SQLConnection:
#     def __init__(self , database_name , database_username , database_password , database_port, databese_host , database_connection_name):
#         self.__engine = create_engine(f"{database_password}://{database_username}:{database_password}@{databese_host}:{database_port}/{database_name}")
