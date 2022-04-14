"""
add_states_table
"""

from yoyo import step

from database.tables import states

__depends__ = {"20220403_01_WoU2o", "__init__"}

steps = [step(states, "DROP table states")]
