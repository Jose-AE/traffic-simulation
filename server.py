from flask import Flask, jsonify

from agents.car_agent import CarAgent, DrivingStyle
from agents.stoplight_agent import StoplightAgent
from maps.city_map import CITY_MAP
from models.city_model import CityModel

model = None
app = Flask(__name__)


def init_model():
    """Initialize the city model."""
    global model
    model = CityModel(CITY_MAP)


def get_map_data():
    """Retrieve map data for cars and stoplights."""
    map_data = {"cars": [], "lights": []}

    for agent in model.schedule.agents:
        if isinstance(agent, StoplightAgent):
            if not agent.is_mirror:
                map_data["lights"].append(
                    {
                        "id": int(agent.unique_id.split("_")[1]),
                        "state": agent.state.name,
                    }
                )

        elif isinstance(agent, CarAgent):
            map_data["cars"].append(
                {
                    "posX": agent.pos[0],
                    "posY": agent.pos[1],
                    "id": int(agent.unique_id.split("_")[1]),
                    "dirX": agent.direction[0],
                    "dirY": agent.direction[1],
                }
            )

    # Sort by id
    map_data["cars"].sort(key=lambda car: car["id"])
    map_data["lights"].sort(key=lambda light: light["id"])

    return map_data


@app.route("/map-data", methods=["GET"])
def get_map_data_route():
    """Handle requests for map data."""
    data = get_map_data()
    model.step()
    return jsonify(data)


@app.route("/reset", methods=["GET"])
def reset_model():
    """Reset the model."""
    init_model()  # Reinitialize the model
    return jsonify({"message": "Model has been reset."})


if __name__ == "__main__":
    init_model()
    app.run()
