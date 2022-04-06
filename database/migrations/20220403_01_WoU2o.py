"""
add-users
"""

from yoyo import step

from database.tables import users

__depends__ = {}

steps = [step(users, "DROP TABLE users")]
