from enum import Enum
import mesa


class StoplightState(Enum):
    GREEN = "green"
    YELLOW = "yellow"
    RED = "red"


class StoplightMode(Enum):
    CLOCK = "clock"
    SMART = "smart"


class StoplightAgent(mesa.Agent):
    def __init__(self, unique_id, model, is_mirror):
        super().__init__(unique_id, model)

        self.state: StoplightState = StoplightState.GREEN
        self.mode: StoplightMode = StoplightMode.CLOCK
        self.is_mirror = is_mirror

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

    def step(self):
        if self.is_mirror:
            self.copy_neighbor()
        elif self.mode == StoplightMode.CLOCK:
            self.clock_activation()
        elif self.mode == StoplightMode.SMART:
            pass
