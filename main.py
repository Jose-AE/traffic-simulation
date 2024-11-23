from mesa.visualization import CanvasGrid, ModularServer
from mesa.visualization.UserParam import NumberInput
from mesa.visualization.UserParam import Choice
from mesa.visualization.modules import ChartModule

from agents.building_agent import BuildingAgent
from agents.car_agent import CarAgent
from agents.parking_agent import ParkingAgent
from agents.road_agent import RoadAgent
from agents.stoplight_agent import StoplightAgent
from map import COMPLEX_MAP, SIMPLE_MAP, CITY_MAP
from models.city_model import CityModel


MAP = CITY_MAP


GRID_WIDTH = len(MAP[0])
GRID_HEIGHT = len(MAP)


def agent_portrayal(agent):

    if isinstance(agent, BuildingAgent):
        portrayal = {
            "Shape": "rect",
            "Color": "black",
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
            "Color": "gray",
            "text": agent.get_directions_string(),
            "text_color": "white",
            "Layer": 0,
        }

    elif isinstance(agent, ParkingAgent):
        portrayal = {
            "Shape": "rect",
            "w": 0.9,  # Width of 1 cell
            "h": 0.9,  # Height of 1 cell
            "Filled": "true",
            "Color": "blue",
            "text": str(agent.unique_id),
            "text_color": "black",
            "Layer": 1,
        }

    elif isinstance(agent, StoplightAgent):

        portrayal = {
            "Shape": "rect",
            "w": 0.5,  # Width of 1 cell
            "h": 0.5,  # Height of 1 cell
            "Filled": "true",
            "Color": agent.state,
            "text": str(agent.unique_id),
            "text_color": "black",
            "Layer": 1,
        }

    elif isinstance(agent, CarAgent):

        portrayal = portrayal = {
            "Shape": "arrowHead",
            "Filled": "true",
            "Color": "white",
            "scale": 0.3,  # Size of the arrow
            "heading_x": agent.direction[0],  # X direction of arrow (0-1)
            "heading_y": agent.direction[1],  # Y direction of arrow (0-1)
            "text": "",
            "text_color": "black",
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


chart_currents = ChartModule(
    [
        {"Label": "Cleaning Efficiency", "Color": "#2563eb"},  # Blue
        {"Label": "Dirt Remaining", "Color": "#dc2626"},  # Red
    ],
    canvas_height=300,
    data_collector_name="datacollector_currents",
)


print(GRID_HEIGHT, GRID_WIDTH)

grid = CanvasGrid(agent_portrayal, GRID_WIDTH, GRID_HEIGHT, 1000, 1000)
server = ModularServer(CityModel, [grid], "Vacuum Model", simulation_params)

server.port = 8521
server.launch(open_browser=False)
