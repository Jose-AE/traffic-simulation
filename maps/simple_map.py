# R-UDRL    -- Road segment: "R" indicates a road, followed by 4 directional movements (U, D, L, R)
#             representing the road's posible movments (if there are repeats they will be ignored)
# P-001U    -- Parking space: "P" indicates parking, followed by a unique ID (e.g., "001"),
#             and the last character (U) represents the direction of the parking spot (U = up).
# L-1LLL    -- Stoplight: "L" indicates a stoplight, followed by an ID (e.g., "1"),
#             and the next 3 characters represent the possible directions (L = left, LLL could mean 3 leftward options).
# BBBBBB    -- Building: "B" represents a building, with no directional or road functionality.


# fmt: off
SIMPLE_MAP: list[list[str]] = [
    ["P-000R", "R-DLDR", "R-LRDL", "P-000L"],
    ["P-000R", "R-LRUL", "R-LRUL", "P-000L"],
]
