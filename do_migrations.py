from yoyo import read_migrations
from yoyo import get_backend
import os

backend = get_backend(os.environ["DB_DSN"])
migrations = read_migrations('database/migrations')

with backend.lock():

    # Apply any outstanding migrations
    backend.apply_migrations(backend.to_apply(migrations))
