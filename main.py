from mesa.visualization import CanvasGrid, ModularServer
from mesa.visualization.UserParam import NumberInput
from mesa.visualization.UserParam import Choice
from mesa.visualization.modules import ChartModule

from agents.building_agent import BuildingAgent
from agents.car_agent import CarAgent
from agents.parking_agent import ParkingAgent
from agents.road_agent import RoadAgent
from agents.stoplight_agent import StoplightAgent
from maps.city_map import CITY_MAP
from models.city_model import CityModel


MAP = CITY_MAP


GRID_WIDTH = len(MAP[0])
GRID_HEIGHT = len(MAP)


def agent_portrayal(agent):

    if isinstance(agent, BuildingAgent):
        portrayal = {
            "Shape": "rect",
            "Color": "#5a9bd5",
            "Filled": "true",
            "Layer": 0,
            "w": 1,  # Width of 1 cell
            "h": 1,  # Height of 1 cell
        }

    elif isinstance(agent, RoadAgent):
        portrayal = {
            "Shape": "rect",
            "w": 1,  # Width of 1 cell
            "h": 1,  # Height of 1 cell
            "Filled": "true",
            "Color": "white",
            "text": agent.get_directions_string(),
            "text_color": "black",
            "Layer": 0,
        }

    elif isinstance(agent, ParkingAgent):
        portrayal = {
            "Shape": "rect",
            "w": 0.9,  # Width of 1 cell
            "h": 0.9,  # Height of 1 cell
            "Filled": "true",
            "Color": "#e3c637",
            "text": agent.unique_id.split("_")[1],
            "text_color": "black",
            "Layer": 1,
        }

    elif isinstance(agent, StoplightAgent):

        portrayal = {
            "Shape": "rect",
            "w": 0.5,  # Width of 1 cell
            "h": 0.5,  # Height of 1 cell
            "Filled": "true",
            "Color": agent.state.value,
            "text": f"({agent.facingDirection[0]},{agent.facingDirection[1]})",  # "M" if agent.is_mirror else f"S{agent.unique_id.split('_')[1]}",
            "text_color": "black",
            "Layer": 1,
        }

    elif isinstance(agent, CarAgent):

        portrayal = portrayal = {
            "Shape": "arrowHead",
            "Filled": "true",
            "Color": agent.get_color(),
            "scale": 0.3,  # Size of the arrow
            "heading_x": agent.direction[0],  # X direction of arrow (0-1)
            "heading_y": agent.direction[1],  # Y direction of arrow (0-1)
            "text": "",  # agent.unique_id,
            "text_color": "red",
            "Layer": 1,
        }

    else:
        portrayal = {
            "Shape": "circle",
            "Filled": "true",
            "Color": "white",
            "r": 0.5,
            "text": "",
            "Layer": 1,
            "text_color": "black",
        }

    return portrayal


simulation_params = {"map": MAP}


charts = ChartModule(
    [
        {"Label": "average_happiness", "Color": "#2563eb"},  # Blue
        {"Label": "average_stress", "Color": "#dc2626"},  # Red
    ],
    canvas_height=300,
    data_collector_name="datacollector",
)


grid = CanvasGrid(agent_portrayal, GRID_WIDTH, GRID_HEIGHT, GRID_WIDTH * 42, GRID_HEIGHT * 42)
server = ModularServer(CityModel, [grid, charts], "Vacuum Model", simulation_params)
server.port = 8521


if __name__ == "__main__":
    server.launch(open_browser=False)
