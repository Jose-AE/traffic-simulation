import mesa


class RoadAgent(mesa.Agent):
    def __init__(self, unique_id, model, directions: set):
        super().__init__(unique_id, model)

        self.directions = directions

    def get_directions_string(self):
        # Map of directions to symbols
        direction_map = {"U": "↑", "D": "↓", "R": "→", "L": "←"}  # Up  # Down  # Right  # Left

        # Convert set of directions to symbols and join into a string
        string = "".join(direction_map[dir] for dir in self.directions if dir in direction_map)
        return string
