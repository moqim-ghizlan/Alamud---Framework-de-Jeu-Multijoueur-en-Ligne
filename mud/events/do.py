from .event import Event2

class DoEvent(Event2):
    NAME = "do"

    def perform(self):
        if not self.object.has_prop("doable"):
            self.add_prop("object-not-doable")
            return self.do_failed()
        if self.object in self.actor:
            self.add_prop("object-already-doable")
            return self.do_failed()
        self.object.move_to(self.actor)
        self.inform("do")

    def do_failed(self):
        self.fail()
        self.inform("do.failed")
