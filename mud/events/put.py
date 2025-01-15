from .event import Event2

class PutEvent(Event2):
    NAME = "put"

    def perform(self):
        if not self.object.has_prop("putable"):
            self.add_prop("object-not-putable")
            return self.put_failed()
        if self.object in self.actor:
            self.add_prop("object-already-putable")
            return self.put_failed()
        self.object.move_to(self.actor)
        self.inform("put")

    def put_failed(self):
        self.fail()
        self.inform("put.failed")
