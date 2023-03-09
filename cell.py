class cell:
    def __init__(self, display_value='.', visible='1', room=-1, trigger=0):
        self.display_value = display_value
        self.visible = visible
        self.room = room
        self.trigger = trigger

    def get_visible(self):
        return self.visible

    def get_display_value(self):
        return self.display_value

    def get_room(self):
        return self.room

    def get_trigger(self):
        return self.trigger

    def set_visible(self, visible):
        self.visible = visible

    def set_room(self, room):
        self.room = room

    def set_trigger(self, trigger):
        self.trigger = trigger

    def fire_trigger(self):
        if self.get_display_value() == "D":
            return "DOOR"
