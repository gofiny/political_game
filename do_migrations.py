import os

from yoyo import get_backend, read_migrations

backend = get_backend(os.environ["DB_DSN"])
migrations = read_migrations("database/migrations")

with backend.lock():

    # Apply any outstanding migrations
    backend.apply_migrations(backend.to_apply(migrations))
