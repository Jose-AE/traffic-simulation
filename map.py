# BBBBBBRRRR    -- Road segment: "R" indicates a road, followed by 4 directional movements (U, D, L, R)
#             representing the road's posible movments (if there are repeats they will be ignored)
# P-001U    -- Parking space: "P" indicates parking, followed by a unique ID (e.g., "001"),
#             and the last character (U) represents the direction of the parking spot (U = up).
# L-1LLL    -- Stoplight: "L" indicates a stoplight, followed by an ID (e.g., "1"),
#             and the next 3 characters represent the possible directions (L = left, LLL could mean 3 leftward options).
# BBBBBB    -- Building: "B" represents a building, with no directional or road functionality.


# fmt: off
SIMPLE_MAP: list[list[str]] = [
    ["R-RRRR", "R-RRRD", "R-RRRD", "R-DDDD"],
    ["R-UUUU", "P-000U", "P-001U", "R-DDDD"],
    ["R-UUUU", "BBBBBB", "BBBBBB", "R-DDDD"],
    ["R-UUUU", "R-LLLL", "R-LLLL", "L-1LLL"],
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
    ["R-DDDD", "R-DDDD", "R-LLDD", "R-LLDD", "R-LLDD", "R-LLDD", "R-LLDD", "R-LLDD", "L-1LDD", "R-LLDD", "R-LLDD", "R-LLDD", "R-LLDD", "R-LLDD", "R-LLDD", "R-LLDD", "R-LLDD", "R-LLDD", "R-LLDD", "R-LLDD", "R-LLDD", "R-LLDD", "R-LLLL", "R-LLLL"],
    ["R-DDDD", "R-DDDD", "R-LLUU", "R-LLUU", "R-LLUU", "R-LLUU", "R-LLUU", "R-LLUU", "L-1LUU", "R-LLUU", "R-LLUU", "R-LLUU", "R-LLUU", "R-LLUU", "R-LLUU", "R-LLUU", "R-LLUU", "R-LLUU", "R-LLUU", "R-LLUU", "R-LLUU", "R-LLUU", "R-LLUU", "R-LLLL"],
    ["R-DDDD", "R-DDDD", "BBBBBB", "P-001U", "BBBBBB", "BBBBBB", "L-1UUU", "L-1UUU", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-DDDD", "R-DDDD", "R-UUUU", "R-UUUU", "BBBBBB", "P-000U", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU"],
    ["R-DDDD", "R-DDDD", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-DDDD", "R-DDDD", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU"],
    ["R-DDDD", "R-DDDD", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "P-000D", "BBBBBB", "R-DDDD", "R-DDDD", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU"],
    ["R-DDDD", "R-DDDD", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU", "L-1LLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-DDDD", "R-DDDD", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "P-000D", "BBBBBB", "R-UUUU", "R-UUUU"],
    ["R-DDDD", "R-DDDD", "BBBBBB", "BBBBBB", "BBBBBB", "P-000R", "R-UUUU", "R-UUUU", "L-1LLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-DDDD", "R-DDDD", "R-UUUU", "R-UUUU", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-UUUU", "R-UUUU"],
    ["R-DDDD", "R-DDDD", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "L-1UUU", "L-1UUU", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-DDDD", "R-DDDD", "R-UUUU", "R-UUUU", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-UUUU", "R-UUUU"],
    ["R-DDDD", "R-DDDD", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU", "P-000L", "BBBBBB", "BBBBBB", "BBBBBB", "R-DDDD", "R-DDDD", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU"],
    ["R-DDDD", "R-DDDD", "P-000L", "BBBBBB", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-DDDD", "R-DDDD", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU"],
    ["R-DDDD", "R-DDDD", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-DDDD", "R-DDDD", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU"],
    ["R-DDDD", "R-DDDD", "BBBBBB", "BBBBBB", "P-000D", "BBBBBB", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "P-000D", "BBBBBB", "R-DDDD", "R-DDDD", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU"],
    ["R-DDDD", "R-DDDD", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLDD", "R-LLLL", "R-LLUU", "R-UULL", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-UUUU", "R-UUUU"],
    ["R-DDDD", "R-DDDD", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLDD", "B#####", "B#####", "R-UUUU", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-UUUU", "R-UUUU"],
    ["R-DDDD", "R-DDDD", "R-RRRR", "R-RRRR", "R-RRRR", "R-RRRR", "R-RRRR", "R-RRRR", "R-RRRR", "R-RRRR", "R-RRRR", "R-RRRR", "R-DDDD", "B#####", "B#####", "R-UURR", "R-RRRR", "L-1RRR", "R-RRRR", "R-RRRR", "R-RRRR", "R-RRRR", "R-UUUU", "R-UUUU"],
    ["R-DDDD", "R-DDDD", "R-RRRR", "R-RRRR", "R-RRRR", "R-RRRR", "R-RRRR", "R-RRRR", "R-RRRR", "R-RRRR", "R-RRRR", "R-RRRR", "R-DDRR", "R-DDRR", "R-RRRR", "R-UURR", "R-RRRR", "L-1RRR", "R-RRRR", "R-RRRR", "R-RRRR", "R-RRRR", "R-UUUU", "R-UUUU"],
    ["R-DDDD", "R-DDDD", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-DDDD", "R-DDDD", "BBBBBB", "BBBBBB", "P-000U", "BBBBBB", "R-DDDD", "R-DDDD", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "L-1UUU", "L-1UUU", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU"],
    ["R-DDDD", "R-DDDD", "BBBBBB", "P-000D", "BBBBBB", "BBBBBB", "R-DDDD", "R-DDDD", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-DDDD", "R-DDDD", "R-UUUU", "R-UUUU", "BBBBBB", "P-000R", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU"],
    ["R-DDDD", "R-DDDD", "L-1LLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-DDDD", "R-DDDD", "R-RRRR", "R-RRRR", "R-RRRR", "R-RRRR", "R-DDDD", "R-DDDD", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU"],
    ["R-DDDD", "R-DDDD", "L-1LLL", "R-LLLL", "R-LLLL", "R-LLLL", "R-DDDD", "R-DDDD", "R-RRRR", "R-RRRR", "R-RRRR", "R-RRRR", "R-DDDD", "R-DDDD", "R-UUUU", "R-UUUU", "BBBBBB", "P-000R", "R-UUUU", "R-UUUU", "P-000L", "BBBBBB", "R-UUUU", "R-UUUU"],
    ["R-DDDD", "R-DDDD", "BBBBBB", "BBBBBB", "P-000U", "BBBBBB", "R-DDDD", "R-DDDD", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "R-DDDD", "R-DDDD", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU"],
    ["R-DDDD", "R-DDDD", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "L-1DDD", "L-1DDD", "BBBBBB", "P-000D", "BBBBBB", "BBBBBB", "R-DDDD", "R-DDDD", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU", "BBBBBB", "BBBBBB", "R-UUUU", "R-UUUU"],
    ["R-RRRR", "R-RRRR", "R-RRDD", "R-RRDD", "R-RRDD", "L-1RDD", "R-RRDD", "R-RRDD", "R-RRDD", "R-RRDD", "R-RRDD", "R-RRDD", "R-RRDD", "R-RRDD", "R-RRDD", "R-RRDD", "R-RRDD", "R-RRDD", "R-RRDD", "R-RRDD", "R-RRDD", "R-RRDD", "R-UURR", "R-UUUU"],
    ["R-RRRR", "R-RRRR", "R-RRUU", "R-RRUU", "R-RRUU", "L-1RUU", "R-RRUU", "R-RRUU", "R-RRUU", "R-RRUU", "R-RRUU", "R-RRUU", "R-RRUU", "R-RRUU", "R-RRUU", "R-RRUU", "R-RRUU", "R-RRUU", "R-RRUU", "R-RRUU", "R-RRUU", "R-RRUU", "R-UURR", "R-UUUU"],
]
