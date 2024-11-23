import mesa

from agents.building_agent import BuildingAgent
from agents.car_agent import CarAgent
from agents.parking_agent import ParkingAgent
from agents.road_agent import RoadAgent
from agents.stoplight_agent import StoplightAgent


class CityModel(mesa.Model):

    def __init__(self, map: list[list[str]], seed=None):
        super().__init__(seed=seed)
        # self.num_agents = n
        self.map_height = len(map)
        self.map_width = len(map[0])
        self.map = self.convert_to_coordinate_system(map)
        self.grid = mesa.space.MultiGrid(self.map_width, self.map_height, False)
        self.schedule = mesa.time.RandomActivation(self)

        self.create_map()
        self.add_cars()

    def create_map(self):

        for y in range(self.map_height):
            for x in range(self.map_width):
                cell_string: str = self.map[y][x]

                if cell_string[0] == "B":
                    a = BuildingAgent(f"({x},{y})", self)
                    self.grid.place_agent(a, (x, y))

                if cell_string[0] == "R":
                    directions = set(cell_string[3:])

                    a = RoadAgent(f"Road({x},{y})", self, directions)
                    self.grid.place_agent(a, (x, y))

                if cell_string[0] == "P":
                    id = int(cell_string[2:5])
                    road_dir = set(cell_string[-1])

                    a = ParkingAgent(id, self)
                    r = RoadAgent(f"Road({x},{y})", self, road_dir)
                    self.grid.place_agent(a, (x, y))
                    self.grid.place_agent(r, (x, y))

                if cell_string[0] == "L":
                    id = int(cell_string[2])
                    directions = set(cell_string[3:])

                    a = StoplightAgent(id, self)
                    r = RoadAgent(f"Road({x},{y})", self, directions)

                    self.grid.place_agent(a, (x, y))
                    self.grid.place_agent(r, (x, y))
                    self.schedule.add(a)  # Add to scheduler if using time steps

    def convert_to_coordinate_system(self, map: list[list]):
        """
        Converts a 2D array map to a coordinate system where [0][0] represents the bottom-left corner.

        This function flips the y-axis of the input array so that the element that was originally
        at the bottom-left corner can be accessed using [0][0] coordinates. The x-axis remains unchanged.
        """

        height = len(map)
        width = len(map[0])

        # Create a new array with the same dimensions
        converted_map = [[None for _ in range(width)] for _ in range(height)]

        # Fill the new array by flipping the y-axis
        for old_y in range(height):
            new_y = height - 1 - old_y  # Flip the y coordinate
            for x in range(width):
                converted_map[new_y][x] = map[old_y][x]

        return converted_map

    def add_cars(self):
        """
        Adds car agents to each parking space in the grid.
        Each car is placed in the same cell as a ParkingAgent.
        """
        # Get all parking agents from the grid
        for cell_contents, pos in self.grid.coord_iter():
            cell_agent = cell_contents[0]  # Get agents in the cell

            # Check if there's a parking agent in this cell
            is_parking = isinstance(cell_agent, ParkingAgent)

            if is_parking:
                car = CarAgent(f"car_{cell_agent.unique_id}", self)
                self.grid.place_agent(car, pos)
                self.schedule.add(car)  # Add to scheduler if using time steps

    def step(self):
        self.schedule.step()
