from typing import Optional
import mesa


class ParkingAgent(mesa.Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

        self.occupied = False

    # def assign_car(self, car_agent):
    #     """Assign a car to this parking spot"""
    #     self.assigned_car_agent = car_agent
    #     return True

    # def unassign_car(self):
    #     """Remove car assignment from this parking spot"""
    #     self.assigned_car_agent = None
