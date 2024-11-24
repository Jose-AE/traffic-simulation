# BBBBBBRRRR    -- Road segment: "R" indicates a road, followed by 4 directional movements (U, D, L, R)
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



# fmt: off
COMPLEX_MAP: list[list[str]] = [
    ["R-RRRR", "R-RRRD", "R-RRRD", "R-DDDD", "L-1LLL", "B-001B", "P-002U"],
    ["R-UUUU", "P-000U", "P-001U", "R-DDDD", "L-2LLR", "R-UDLL", "B-002B"],
    ["R-UUUR", "BBBBBB", "R-RUUR", "L-3LRR", "P-003L", "R-DDLL", "B-003B"],
    ["R-URRR", "R-UDLR", "P-004R", "R-DDDD", "L-4LLR", "B-004B", "R-URUU"],
    ["L-5LLL", "R-DDDL", "L-6LLL", "R-RRRR", "P-005D", "B-005B", "L-7LLL"],
    ["P-006U", "R-RRRD", "R-UURR", "B-006B", "R-ULUL", "L-8LLL", "P-007L"],
    ["R-UDLR", "R-RRRL", "B-007B", "R-URRR", "R-DDDL", "P-008U", "L-9LLL"],
]

# fmt: off
CITY_MAP: list[list[str]] = [
    ["R-DDDD", "R-DDLL", "R-LLLL", "R-LLLD", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "L-1LLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLDD", "R-LLDD", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLD", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL"],
    ["R-DDDD", "R-DDLL", "R-LLLL", "R-LLLD", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "L-1LLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLDD", "R-LLDD", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLD", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLUU", "R-LLUU"],
    ["R-DDDD", "R-DDDD", "BBBBBB", "P-002U", "BBBBBB", "BBBBBB", "L-1UUU", "L-1UUU", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-DDDD", "R-DDDD", "R-UUUU", "R-UUUU", "BBBBBB", "P-012U", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU"],
    ["R-DDDD", "R-DDDD", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-DDDD", "R-DDDD", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU"],
    ["R-DDDD", "R-DDDD", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "P-009D", "BBBBBB", "R-DDDD", "R-DDDD", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU"],
    ["R-DDDD", "R-DDDD", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU", "L-1LLL", "R-LLLL", "R-LLLU", "R-LLLL", "R-DDLL", "R-DDLL", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "P-015D", "BBBBBB", "R-UUUU", "R-UUUU"],
    ["R-DDDD", "R-DDDD", "BBBBBB", "BBBBBB", "BBBBBB", "P-006R", "R-UUUL", "R-UUUL", "L-1LLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-DDLL", "R-DDLL", "R-UUUU", "R-UUUU", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLU", "R-LLLL", "R-UULL", "R-UULL"],
    ["R-DDDD", "R-DDDD", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "L-1UUU", "L-1UUU", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-DDDD", "R-DDDD", "R-UUUU", "R-UUUU", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLD", "R-LLLL", "R-UULL", "R-UULL"],
    ["R-DDDD", "R-DDDD", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUR", "P-007L", "BBBBBB", "BBBBBB", "BBBBBB", "R-DDDD", "R-DDDD", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "P-016U", "BBBBBB", "R-UUUU", "R-UUUU"],
    ["R-DDDR", "R-DDDR", "P-001L", "BBBBBB", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-DDDD", "R-DDDD", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU"],
    ["R-DDDD", "R-DDDD", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-DDDD", "R-DDDD", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU"],
    ["R-DDDD", "R-DDDD", "BBBBBB", "BBBBBB", "P-004D", "BBBBBB", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "P-010D", "BBBBBB", "R-DDDD", "R-DDDD", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU"],
    ["R-DDDD", "R-DDDD", "R-LLLL", "R-LLLL", "R-LLUU", "R-LLLL", "R-LLUU", "R-LLUU", "R-LLLL", "R-LLLL", "R-LLLU", "R-LLLL", "R-LLDD", "R-LLLL", "R-LLUU", "R-UULL", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-UULL", "R-UULL"],
    ["R-DDDD", "R-DDDD", "R-LLLL", "R-LLLL", "R-LLUU", "R-LLLL", "R-LLUU", "R-LLUU", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLDD", "B#####", "B#####", "R-UUUU", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-UULL", "R-UULL"],
    ["R-DDRR", "R-DDRR", "R-RRRR", "R-RRRR", "R-RRRR", "R-RRRR", "R-RRDD", "R-RRDD", "R-RRRR", "R-RRRR", "R-RRRR", "R-RRRR", "R-DDDD", "B#####", "B#####", "R-UURR", "R-RRRR", "L-1RRR", "R-RRRR", "R-RRRR", "R-RRRR", "R-RRRR", "R-UUUU", "R-UUUU"],
    ["R-DDRR", "R-DDRR", "R-RRRR", "R-RRRR", "R-RRRR", "R-RRRR", "R-RRDD", "R-RRDD", "R-RRRR", "R-RRRR", "R-RRRD", "R-RRRR", "R-DDRR", "R-DDRR", "R-RRRR", "R-UURR", "R-RRRR", "L-1RRR", "R-RRRR", "R-RRRR", "R-RRRR", "R-RRRR", "R-UUUU", "R-UUUU"],
    ["R-DDDD", "R-DDDD", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-DDDD", "R-DDDD", "BBBBBB", "BBBBBB", "P-011U", "BBBBBB", "R-DDDD", "R-DDDD", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "L-1UUU", "L-1UUU", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU"],
    ["R-DDDD", "R-DDDD", "BBBBBB", "P-003D", "BBBBBB", "BBBBBB", "R-DDDD", "R-DDDD", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-DDDD", "R-DDDD", "R-UUUU", "R-UUUU", "BBBBBB", "P-013R", "R-UUUL", "R-UUUL", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU"],
    ["R-DDDD", "R-DDDD", "L-1LLL", "R-LLLU", "R-LLLD", "R-LLLL", "R-DRLL", "R-DRDL", "R-RRRR", "R-RRRR", "R-RRRR", "R-RRRR", "R-DDDD", "R-DDDD", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU"],
    ["R-DDDD", "R-DDDD", "L-1LLL", "R-LLLU", "R-LLLD", "R-LLLL", "R-DRLL", "R-DRDL", "R-RRRR", "R-RRRR", "R-RRRR", "R-RRRR", "R-DDDD", "R-DDDD", "R-UUUU", "R-UUUU", "BBBBBB", "P-014R", "R-UUUL", "R-UUUR", "P-017L", "BBBBBB", "R-UUUU", "R-UUUU"],
    ["R-DDDD", "R-DDDD", "BBBBBB", "BBBBBB", "P-005U", "BBBBBB", "R-DDDD", "R-DDDD", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-DDDD", "R-DDDD", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU"],
    ["R-DDDD", "R-DDDD", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "L-1DDD", "L-1DDD", "BBBBBB", "P-008D", "BBBBBB", "BBBBBB", "R-DDDD", "R-DDDD", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU"],
    ["R-RRDD", "R-RRDD", "R-RRRR", "R-RRRR", "R-RRRR", "L-1RRR", "R-RRRR", "R-RRRR", "R-RRRR", "R-RRRU", "R-RRRR", "R-RRRR", "R-RRRR", "R-RRRR", "R-RRUU", "R-RRUU", "R-RRRR", "R-RRRR", "R-RRUU", "R-RRUU", "R-RRRR", "R-RRRR", "R-UURR", "R-UUUU"],
    ["R-RRRR", "R-RRRR", "R-RRRR", "R-RRRR", "R-RRRR", "L-1RRR", "R-RRRR", "R-RRRR", "R-RRRR", "R-RRRU", "R-RRRR", "R-RRRR", "R-RRRR", "R-RRRR", "R-RRUU", "R-RRUU", "R-RRRR", "R-RRRR", "R-RRUU", "R-RRUU", "R-RRRR", "R-RRRR", "R-UURR", "R-UUUU"],
]
