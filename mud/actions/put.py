from .action import Action2
from mud.events import PutEvent


class PutAction(Action2):
    EVENT = PutEvent
    ACTION = "put"
    RESOLVE_OBJECT = "resolve_for_operate"
