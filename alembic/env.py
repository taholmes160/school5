from sqlalchemy import engine_from_config, pool
from logging.config import fileConfig
from alembic import context

# Import your app creator function and database models
from app.app_creator import create_app
from models import db

# Initialize the Flask app and get the SQLAlchemy metadata
app, _ = create_app()
target_metadata = db.metadata

# Set up Alembic configuration
config = context.config
config.set_main_option("sqlalchemy.url", str(app.config['SQLALCHEMY_DATABASE_URI']))
fileConfig(config.config_file_name)

def run_migrations_online():
    # Create an engine with the Flask app's configuration
    engine = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool
    )

    # Connect to the database engine
    connection = engine.connect()
    context.configure(
        connection=connection,
        target_metadata=target_metadata
    )

    try:
        # Run the migrations
        with context.begin_transaction():
            context.run_migrations()
    finally:
        # Close the database connection
        connection.close()

# Run migrations online
run_migrations_online()
