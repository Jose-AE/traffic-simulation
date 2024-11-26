from enum import Enum
import math
import mesa


class StoplightState(Enum):
    GREEN = "green"
    YELLOW = "yellow"
    RED = "red"


class StoplightMode(Enum):
    CLOCK = "clock"
    SMART = "smart"


class StoplightAgent(mesa.Agent):

    def __init__(self, unique_id, model, is_mirror, roadDrection):
        super().__init__(unique_id, model)

        self.state: StoplightState = StoplightState.GREEN
        self.mode: StoplightMode = StoplightMode.CLOCK  # Default to SMART mode
        self.is_mirror = is_mirror

        # Direction mapping
        direction_map = {"U": (0, -1), "D": (0, 1), "L": (1, 0), "R": (-1, 0)}
        self.facingDirection: tuple[int, int] = direction_map.get(roadDrection, (0, 0))

        # Smart mode specific attributes
        self.estimated_arrival_time = None
        self.green_duration = 2
        self.yellow_duration = 2
        self.red_duration = 5
        self.detection_range = 2

        self.current_cycle_step = 0

    def calculate_estimated_arrival_time(self, car):
        """
        Calculate the estimated time of arrival for a car.

        Args:
            car (CarAgent): The car agent approaching the intersection

        Returns:
            float: Estimated time of arrival
        """
        # Calculate distance to intersection
        dx = abs(car.pos[0] - self.pos[0])
        dy = abs(car.pos[1] - self.pos[1])
        distance = math.sqrt(dx**2 + dy**2)

        # Assume constant speed (adjust based on your car agent's implementation)
        speed = 1  # cells per step
        estimated_arrival = distance / speed

        return estimated_arrival

    def smart_activation(self):
        """
        Smart mode logic for stoplight state management
        """
        # Get nearby cars
        nearby_cars = self.get_nearby_cars()

        # If no cars nearby, stay on yellow
        if not nearby_cars:
            self.state = StoplightState.YELLOW
            return

        # Find the car with the earliest estimated arrival time
        nearest_car = min(nearby_cars, key=lambda car: self.calculate_estimated_arrival_time(car))

        # Calculate estimated arrival time for the nearest car
        self.estimated_arrival_time = self.calculate_estimated_arrival_time(nearest_car)

        # Manage traffic light cycle based on car arrival
        if self.current_cycle_step < self.green_duration:
            self.state = StoplightState.GREEN
        elif self.current_cycle_step < self.green_duration + self.yellow_duration:
            self.state = StoplightState.YELLOW
        else:
            self.state = StoplightState.RED

        # Increment cycle step
        self.current_cycle_step = (self.current_cycle_step + 1) % (
            self.green_duration + self.yellow_duration + self.red_duration
        )

    def clock_activation(self):
        cycle_length = 12  # 5 (green) + 2 (yellow) + 5 (red)
        current_step = self.model.schedule.steps % cycle_length

        if current_step < 5:
            self.state = StoplightState.GREEN
        elif current_step < 7:
            self.state = StoplightState.YELLOW
        else:
            self.state = StoplightState.RED

    def copy_neighbor(self):
        neighbor_positions = self.model.grid.get_neighborhood(
            self.pos, moore=False, include_center=False
        )

        # Get all stoplight agents from neighboring cells
        neighbor_stoplights = []
        for pos in neighbor_positions:
            cell_contents = self.model.grid.get_cell_list_contents(pos)
            for agent in cell_contents:
                if isinstance(agent, StoplightAgent) and not agent.is_mirror:
                    neighbor_stoplights.append(agent)

        if neighbor_stoplights:
            self.state = neighbor_stoplights[0].state

    def get_nearby_cars(self):
        """
        Get all cars in the same direction as the stoplight up to 3 cells.

        Returns:
            list: A list of car agents within 3 cells in the stoplight's facing direction
        """
        from agents.car_agent import CarAgent

        nearby_cars = []

        # Calculate the direction vector
        dx, dy = self.facingDirection

        # Check up to 3 cells in the facing direction
        for distance in range(1, self.detection_range + 1):
            check_pos = (self.pos[0] + dx * distance, self.pos[1] + dy * distance)

            # Check if the position is within the grid
            if self.model.grid.out_of_bounds(check_pos):
                break

            # Get contents of the cell
            cell_contents = self.model.grid.get_cell_list_contents([check_pos])

            # Find car agents in the cell
            cars_in_cell = [agent for agent in cell_contents if isinstance(agent, CarAgent)]

            # Add cars to the list
            nearby_cars.extend(cars_in_cell)

        return nearby_cars

    def step(self):
        # if self.is_mirror and self.mode != StoplightMode.SMART:
        #     self.copy_neighbor()
        if self.mode == StoplightMode.CLOCK:
            self.clock_activation()
        elif self.mode == StoplightMode.SMART:
            self.smart_activation()
