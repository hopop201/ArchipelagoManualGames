from BaseClasses import Location
from .Data import location_table
from .Game import starting_index

######################
# Generate location lookups
######################

count = starting_index + 500 # 500 each for items and locations
custom_victory_location = {}
victory_key = {}

# add sequential generated ids to the lists
for key, _ in enumerate(location_table):
    if "victory" in location_table[key] and location_table[key]["victory"]:
        custom_victory_location = location_table[key]
        victory_key = key # store the victory location to be removed later
        
        continue

    location_table[key]["id"] = count
    location_table[key]["region"] = "Manual" # all locations are in the same region for Manual
    count += 1

if victory_key:
    location_table.pop(victory_key)

# Add the game completion location, which will have the Victory item assigned to it automatically
location_table.append({
    "id": count + 1,
    "name": "__Manual Game Complete__",
    "region": "Manual",
    "requires": custom_victory_location["requires"] if "requires" in custom_victory_location else []
})

location_id_to_name = {}
for item in location_table:
    location_id_to_name[item["id"]] = item["name"]

# location_id_to_name[None] = "__Manual Game Complete__"
location_name_to_id = {name: id for id, name in location_id_to_name.items()}

######################
# Location classes
######################


class ManualLocation(Location):
    game = "Manual"
