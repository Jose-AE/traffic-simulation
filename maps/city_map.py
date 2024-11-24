# R-UDRL    -- Road segment: "R" indicates a road, followed by 4 directional movements (U, D, L, R)
#             representing the road's posible movments (if there are repeats they will be ignored)
# P-001U    -- Parking space: "P" indicates parking, followed by a unique ID (e.g., "001"),
#             and the last character (U) represents the direction of the parking spot (U = up).
# LM-00L    -- Mirror Stoplight: "LM" indicates a mirror stoplight (copies adjacent), followed by road direction (e.g., "L" for left)
# LS-00L   -- Standard Stoplight: "LS" indicates a regular stoplight, followed by ID ("00") and road direction (e.g., "L" for left)
#             and the next 3 characters represent the possible directions (L = left, LLL could mean 3 leftward options).
# BBBBBB    -- Building: "B" represents a building, with no directional or road functionality.


# fmt: off
CITY_MAP: list[list[str]] = [
    ["R-DDDD", "R-DDLL", "R-LLLL", "R-LLLD", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "LS-00L", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLDD", "R-LLDD", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLD", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL"],
    ["R-DDDD", "R-DDLL", "R-LLLL", "R-LLLD", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "LM-00L", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLDD", "R-LLDD", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLD", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLUU", "R-LLUU"],
    ["R-DDDD", "R-DDDD", "BBBBBB", "P-002U", "BBBBBB", "BBBBBB", "LS-01U", "LM-01U", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-DDDD", "R-DDDD", "R-UUUU", "R-UUUU", "BBBBBB", "P-012U", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU"],
    ["R-DDDD", "R-DDDD", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-DDDD", "R-DDDD", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU"],
    ["R-DDDD", "R-DDDD", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "P-009D", "BBBBBB", "R-DDDD", "R-DDDD", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU"],
    ["R-DDDD", "R-DDDD", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU", "LM-03L", "R-LLLL", "R-LLLU", "R-LLLL", "R-DDLL", "R-DDLL", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "P-015D", "BBBBBB", "R-UUUU", "R-UUUU"],
    ["R-DDDD", "R-DDDD", "BBBBBB", "BBBBBB", "BBBBBB", "P-006R", "R-UUUL", "R-UUUL", "LS-03L", "R-LLLL", "R-LLLL", "R-LLLL", "R-DDLL", "R-DDLL", "R-UUUU", "R-UUUU", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLU", "R-LLLL", "R-UULL", "R-UULL"],
    ["R-DDDD", "R-DDDD", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "LS-02U", "LM-02U", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-DDDD", "R-DDDD", "R-UUUU", "R-UUUU", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLD", "R-LLLL", "R-UULL", "R-UULL"],
    ["R-DDDD", "R-DDDD", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUR", "P-007L", "BBBBBB", "BBBBBB", "BBBBBB", "R-DDDD", "R-DDDD", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "P-016U", "BBBBBB", "R-UUUU", "R-UUUU"],
    ["R-DDDR", "R-DDDR", "P-001L", "BBBBBB", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-DDDD", "R-DDDD", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU"],
    ["R-DDDD", "R-DDDD", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-DDDD", "R-DDDD", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU"],
    ["R-DDDD", "R-DDDD", "BBBBBB", "BBBBBB", "P-004D", "BBBBBB", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "P-010D", "BBBBBB", "R-DDDD", "R-DDDD", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU"],
    ["R-DDDD", "R-DDDD", "R-LLLL", "R-LLLL", "R-LLUU", "R-LLLL", "R-LLUU", "R-LLUU", "R-LLLL", "R-LLLL", "R-LLLU", "R-LLLL", "R-LLDD", "R-LLLL", "R-LLUU", "R-UULL", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-UULL", "R-UULL"],
    ["R-DDDD", "R-DDDD", "R-LLLL", "R-LLLL", "R-LLUU", "R-LLLL", "R-LLUU", "R-LLUU", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLDD", "B#####", "B#####", "R-UUUU", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-UULL", "R-UULL"],
    ["R-DDRR", "R-DDRR", "R-RRRR", "R-RRRR", "R-RRRR", "R-RRRR", "R-RRDD", "R-RRDD", "R-RRRR", "R-RRRR", "R-RRRR", "R-RRRR", "R-DDDD", "B#####", "B#####", "R-UURR", "R-RRRR", "LS-04R", "R-RRRR", "R-RRRR", "R-RRRR", "R-RRRR", "R-UUUU", "R-UUUU"],
    ["R-DDRR", "R-DDRR", "R-RRRR", "R-RRRR", "R-RRRR", "R-RRRR", "R-RRDD", "R-RRDD", "R-RRRR", "R-RRRR", "R-RRRD", "R-RRRR", "R-DDRR", "R-DDRR", "R-RRRR", "R-UURR", "R-RRRR", "LM-04R", "R-RRRR", "R-RRRR", "R-RRRR", "R-RRRR", "R-UUUU", "R-UUUU"],
    ["R-DDDD", "R-DDDD", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-DDDD", "R-DDDD", "BBBBBB", "BBBBBB", "P-011U", "BBBBBB", "R-DDDD", "R-DDDD", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "LS-05U", "LM-05U", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU"],
    ["R-DDDD", "R-DDDD", "BBBBBB", "P-003D", "BBBBBB", "BBBBBB", "R-DDDD", "R-DDDD", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-DDDD", "R-DDDD", "R-UUUU", "R-UUUU", "BBBBBB", "P-013R", "R-UUUL", "R-UUUL", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU"],
    ["R-DDDD", "R-DDDD", "LS-06L", "R-LLLU", "R-LLLD", "R-LLLL", "R-DRLL", "R-DRDL", "R-RRRR", "R-RRRR", "R-RRRR", "R-RRRR", "R-DDDD", "R-DDDD", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU"],
    ["R-DDDD", "R-DDDD", "LM-06L", "R-LLLU", "R-LLLD", "R-LLLL", "R-DRLL", "R-DRDL", "R-RRRR", "R-RRRR", "R-RRRR", "R-RRRR", "R-DDDD", "R-DDDD", "R-UUUU", "R-UUUU", "BBBBBB", "P-014R", "R-UUUL", "R-UUUR", "P-017L", "BBBBBB", "R-UUUU", "R-UUUU"],
    ["R-DDDD", "R-DDDD", "BBBBBB", "BBBBBB", "P-005U", "BBBBBB", "R-DDDD", "R-DDDD", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-DDDD", "R-DDDD", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU"],
    ["R-DDDD", "R-DDDD", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "LS-08D", "LM-08D", "BBBBBB", "P-008D", "BBBBBB", "BBBBBB", "R-DDDD", "R-DDDD", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU"],
    ["R-RRDD", "R-RRDD", "R-RRRR", "R-RRRR", "R-RRRR", "LS-07R", "R-RRRR", "R-RRRR", "R-RRRR", "R-RRRU", "R-RRRR", "R-RRRR", "R-RRRR", "R-RRRR", "R-RRUU", "R-RRUU", "R-RRRR", "R-RRRR", "R-RRUU", "R-RRUU", "R-RRRR", "R-RRRR", "R-UURR", "R-UUUU"],
    ["R-RRRR", "R-RRRR", "R-RRRR", "R-RRRR", "R-RRRR", "LM-07R", "R-RRRR", "R-RRRR", "R-RRRR", "R-RRRU", "R-RRRR", "R-RRRR", "R-RRRR", "R-RRRR", "R-RRUU", "R-RRUU", "R-RRRR", "R-RRRR", "R-RRUU", "R-RRUU", "R-RRRR", "R-RRRR", "R-UURR", "R-UUUU"],
]
