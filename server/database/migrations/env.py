from logging.config import fileConfig
import os
from dotenv import load_dotenv
from alembic import context
from sqlalchemy import pool, engine_from_config
from app.db import Base    # importa o metadata

# -------- load .env --------
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '..', '.env'))
context.config.set_main_option("sqlalchemy.url", os.getenv("DATABASE_URL"))
# ---------------------------

fileConfig(context.config.config_file_name)
target_metadata = Base.metadata
config_attrs = context.config.get_section(context.config.config_ini_section)

def run_migrations_online():
    connectable = engine_from_config(
        config_attrs, prefix="sqlalchemy.", poolclass=pool.NullPool
    )
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()
