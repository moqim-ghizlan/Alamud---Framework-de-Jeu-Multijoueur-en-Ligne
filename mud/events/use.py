from .event import Event2

class UseEvent(Event2):
    NAME = "use"

    def perform(self):
        if not self.object.has_prop("usable"):
            self.add_prop("object-not-usable")
            return self.use_failed()
        if self.object in self.actor:
            self.add_prop("object-already-usable")
            return self.use_failed()
        self.object.move_to(self.actor)
        self.inform("use")

    def use_failed(self):
        self.fail()
        self.inform("use.failed")
