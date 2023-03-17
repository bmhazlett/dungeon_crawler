class Game:
    def __init__(self, floors, curr_floor, floor_mapping):
        self.floors = floors
        self.curr_floor = curr_floor
        self.floor_mapping = floor_mapping

    def get_floors(self):
        return self.floors

    def get_curr_floor(self):
        return self.curr_floor

    def get_floor_mapping(self):
        return self.floor_mapping

    def set_floors(self, floors):
        self.floors = floors

    def set_curr_floor(self, curr_floor):
        self.curr_floor = curr_floor

    def set_floor_mapping(self, floor_mapping):
        self.floor_mapping = floor_mapping

    def move_next_floor(self, x, y):
        floor_name = self.curr_floor.get_floor_name()
        next_floor = self.floor_mapping[floor_name]["stairs"][str(x) + "," + str(y)]
        for floor in self.floors:
            if floor.get_floor_name() == next_floor:
                self.set_curr_floor(floor)
