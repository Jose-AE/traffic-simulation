import mesa

from agents.road_agent import RoadAgent


class CarAgent(mesa.Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

        # Create the agent's variable and set the initial values.
        self.direction = [0, 1]

    def random_move(self):
        possible_steps = self.get_possible_moves()

        new_position = self.random.choice(possible_steps)
        self.update_direction(new_position)
        self.model.grid.move_agent(self, new_position)

    def get_possible_moves(self) -> list[list[int, int]]:
        cell_contents = self.model.grid.get_cell_list_contents([self.pos])
        road = [obj for obj in cell_contents if isinstance(obj, RoadAgent)][0]

        moves = []

        # Check if the road agent allows movement in certain directions
        if road:
            # Make sure there is at least one RoadAgent and check its directions
            if "L" in road.directions:
                # Example move for "L" direction: move left by one unit
                moves.append([self.pos[0] - 1, self.pos[1]])

            if "R" in road.directions:
                # Example move for "R" direction: move right by one unit
                moves.append([self.pos[0] + 1, self.pos[1]])

            if "U" in road.directions:
                # Example move for "U" direction: move up by one unit
                moves.append([self.pos[0], self.pos[1] + 1])

            if "D" in road.directions:
                # Example move for "D" direction: move down by one unit
                moves.append([self.pos[0], self.pos[1] - 1])

        return moves

    def update_direction(self, new_position):
        # Calculate the direction based on the new position and current position
        x_diff = new_position[0] - self.pos[0]
        y_diff = new_position[1] - self.pos[1]

        # Update the direction based on the differences in coordinates
        if x_diff == -1:
            self.direction = [-1, 0]  # Left (L)
        elif x_diff == 1:
            self.direction = [1, 0]  # Right (R)
        elif y_diff == 1:
            self.direction = [0, 1]  # Up (U)
        elif y_diff == -1:
            self.direction = [0, -1]  # Down (D)

    def step(self):
        self.random_move()
        print("car move")
