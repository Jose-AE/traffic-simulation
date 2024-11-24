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
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

        self.state: StoplightState = StoplightState.GREEN
        self.mode: StoplightMode = StoplightMode.CLOCK

    def clock_activation(self):
        if self.model.schedule.steps % 10 == 0:
            self.state = (
                StoplightState.RED if self.state == StoplightState.GREEN else StoplightState.GREEN
            )

    def step(self):

        if self.mode == StoplightMode.CLOCK:
            self.clock_activation()
        elif self.mode == StoplightMode.SMART:
            pass
