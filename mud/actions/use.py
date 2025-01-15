from .action import Action2
from mud.events import UseEvent

class UseAction(Action2):
    EVENT = UseEvent
    RESOLVE_OBJECT = "resolve_for_operate"
    ACTION = "use"
