from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

atletas = Table("atletas", meta,    #la tabla se llamara atletas. #meta es una propiedad de MetaData ver en config.db
        Column("id", Integer, primary_key=True),
        Column("name", String(255)),
        Column("email", String(255)),
        Column("date", String(255)))

meta.create_all(engine)