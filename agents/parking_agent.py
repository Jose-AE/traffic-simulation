from typing import Optional
import mesa


class ParkingAgent(mesa.Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

        self.occupied = False
