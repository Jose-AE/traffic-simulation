from collections import deque
from typing import Optional
import mesa

from agents.parking_agent import ParkingAgent
from agents.road_agent import RoadAgent
from enum import Enum

from agents.stoplight_agent import StoplightAgent, StoplightState


class DrivingStyle(Enum):
    COOPERATIVE = "cooperative"  # Prefers yielding
    AGGRESSIVE = "aggressive"  # Prefers pushing through
    CAUTIOUS = "cautious"  # Prefers safe routes
    OPPORTUNISTIC = "opportunistic"  # Maximizes personal gain
    RECKLESS = "reckless"  # May ignore red lights if stressed


class DriverState(Enum):
    HAPPY = "green"
    ANGRY = "red"
    IMPATIENT = "orange"
    NORMAL = "black"


class CarAgent(mesa.Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

        # Create the agent's variable and set the initial values.
        self.destination: Optional[tuple[int, int]] = None
        self.direction: tuple[int, int] = (0, 1)
        self.path: Optional[list[tuple[int, int]]] = []
        self.assigned_parking_spot = None

        # Stats
        self.driving_style: DrivingStyle = DrivingStyle.COOPERATIVE
        self.patience = self.get_initial_patience()

        self.init_stats()

    def random_move(self):
        """Simple  behaviour, just move the car in a random dir"""
        possible_steps = self.get_possible_moves(self.pos)

        new_position = self.random.choice(possible_steps)
        self.update_direction(new_position)
        self.model.grid.move_agent(self, new_position)

    def get_possible_moves(self, pos) -> list[tuple[int, int]]:
        cell_contents = self.model.grid.get_cell_list_contents([pos])
        road = [obj for obj in cell_contents if isinstance(obj, RoadAgent)][0]

        moves = []

        # Check if the road agent allows movement in certain directions
        if road:
            # Make sure there is at least one RoadAgent and check its directions
            if "L" in road.directions:
                # Example move for "L" direction: move left by one unit
                moves.append((pos[0] - 1, pos[1]))

            if "R" in road.directions:
                # Example move for "R" direction: move right by one unit
                moves.append((pos[0] + 1, pos[1]))

            if "U" in road.directions:
                # Example move for "U" direction: move up by one unit
                moves.append((pos[0], pos[1] + 1))

            if "D" in road.directions:
                # Example move for "D" direction: move down by one unit
                moves.append((pos[0], pos[1] - 1))

        return moves

    def update_direction(self, new_position):
        # Calculate the direction based on the new position and current position
        x_diff = new_position[0] - self.pos[0]
        y_diff = new_position[1] - self.pos[1]

        # Update the direction based on the differences in coordinates
        if x_diff == -1:
            self.direction = (-1, 0)  # Left (L)
        elif x_diff == 1:
            self.direction = (1, 0)  # Right (R)
        elif y_diff == 1:
            self.direction = (0, 1)  # Up (U)
        elif y_diff == -1:
            self.direction = (0, -1)  # Down (D)

    def set_destination(self):
        """
        Set the cars destination to a random parking spot
        """

        parking_positions = [
            pos
            for cell_contents, pos in self.model.grid.coord_iter()
            if cell_contents  # Check if cell is not empty
            and any(isinstance(obj, ParkingAgent) and not obj.occupied for obj in cell_contents)
            and pos != self.pos
        ]

        if parking_positions:
            # Assign a random parking spot as the destination
            dest = self.random.choice(parking_positions)
            self.destination = dest

            # Get the ParkingAgent at this position and mark it as occupied
            cell_contents = self.model.grid.get_cell_list_contents([dest])
            parking_spot = next(obj for obj in cell_contents if isinstance(obj, ParkingAgent))
            parking_spot.occupied = True

            # print(f"{self.unique_id} is going to park_{parking_spot.unique_id}")

        else:
            self.destination = None

    def check_for_stop_light(self, pos: tuple[int, int]) -> bool:
        """
        Determines whether the agent should proceed based on the state of a stoplight at the given position.

        Args:
            pos (tuple[int, int]): The grid position to check for a stoplight.

        Returns:
            bool: True if the agent can proceed, False otherwise.
        """

        cell_contents = self.model.grid.get_cell_list_contents(pos)
        stop_light = next(
            (agent for agent in cell_contents if isinstance(agent, StoplightAgent)), None
        )

        if not stop_light or stop_light.state == StoplightState.GREEN:
            return True

        elif stop_light.state == StoplightState.RED:
            self.time_waiting += 1
            self.happiness = max(0, self.happiness - 5)
            self.stress += 2 if self.driving_style == DrivingStyle.AGGRESSIVE else 1
            return False

        if stop_light.state == StoplightState.YELLOW:
            if self.driving_style == DrivingStyle.RECKLESS:
                return self.random.random() < (self.stress / 100 + 0.3)
            return False

    def get_color(self) -> str:
        """
        Get the current color based on the emotional state
        """
        return self.state.value

    def get_initial_patience(self) -> int:
        """Set initial patience based on personality."""
        base_patience = self.random.randint(3, 8)
        modifiers = {
            DrivingStyle.COOPERATIVE.name: 2,
            DrivingStyle.AGGRESSIVE.name: -2,
            DrivingStyle.CAUTIOUS.name: 3,
            DrivingStyle.OPPORTUNISTIC.name: 0,
            DrivingStyle.RECKLESS.name: -3,
        }
        return max(1, base_patience + modifiers[self.driving_style.name])

    def init_stats(self):
        self.time_waiting = 0
        self.state: DriverState = DriverState.NORMAL
        self.happiness = 100
        self.stress = 0

    def update_emotional_state(self):
        # Update stress based on personality
        stress_factor = 2 if self.driving_style == DrivingStyle.AGGRESSIVE else 1
        self.stress += self.time_waiting * stress_factor
        self.stress = min(100, max(0, self.stress))

        # Update state
        if self.happiness > 80 and self.stress < 30:
            self.state = DriverState.HAPPY
        elif self.happiness < 30 or self.stress > 70:
            self.state = DriverState.ANGRY
        elif self.time_waiting > self.patience:
            self.state = DriverState.IMPATIENT
        else:
            self.state = DriverState.NORMAL

    def check_for_collision(self, pos: tuple[int, int]):
        """
        Checks if there is another car at the given position.
        """
        # Default to current position if no position is specified

        # Get the contents of the cell at the position
        cell_contents = self.model.grid.get_cell_list_contents([pos])

        # Check if there is any other CarAgent in the cell
        for agent in cell_contents:
            if isinstance(agent, CarAgent) and agent != self:
                return True  # Collision detected

        return False  # No collision

    def calculate_path(self):
        """
        Calculate the shortest path to the destination using BFS.
        Updates the agent's path attribute with the calculated route.
        """

        queue = deque([[self.pos]])  # [    [(1,2),(1,2)],  [(1,2),(1,2)]    ]
        visited = set()  # Set to keep track of visited positions
        visited.add(self.pos)

        while queue:
            # Get the current path
            path = queue.popleft()
            current = path[-1]  # The last position in the path

            # If we've reached the end, return the path
            if current == self.destination:
                self.path = path[1:]  # return path excluding current pos (give future moves)
                ##print(f"path calculated for {self.unique_id} and path is {0}")
                return

            for neighbor in self.get_possible_moves(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(path + [neighbor])

        # If no path is found, return an empty list
        self.path = []
        if self.destination != None:
            print(f"path not found for {self.unique_id} dest was {self.destination} ")

    def move(self):
        if not self.destination:
            self.init_stats()
            self.set_destination()

        self.calculate_path()
        if len(self.path) > 0:  # if has not reached path
            next_pos = self.path[0]

            if not self.check_for_collision(next_pos) and self.check_for_stop_light(next_pos):
                self.update_direction(next_pos)
                self.model.grid.move_agent(self, next_pos)
        else:
            self.destination = None

    def step(self):
        self.update_emotional_state()
        self.move()
