# List of district cities in Portugal with rounded latitude and longitude
cities_portugal = [
    {"city": "Lisbon", "lat": round(38.736946, 2), "lon": round(-9.142685, 2)},
    {"city": "Porto", "lat": round(41.157944, 2), "lon": round(-8.629105, 2)},
    {"city": "Braga", "lat": round(41.550323, 2), "lon": round(-8.420052, 2)},
    {"city": "Coimbra", "lat": round(40.205642, 2), "lon": round(-8.419551, 2)},
    {"city": "Faro", "lat": round(37.017963, 2), "lon": round(-7.930834, 2)},
    {"city": "Evora", "lat": round(38.571389, 2), "lon": round(-7.913611, 2)},
    {"city": "Leiria", "lat": round(39.743621, 2), "lon": round(-8.807051, 2)},
    {"city": "Aveiro", "lat": round(40.640506, 2), "lon": round(-8.653754, 2)},
    {"city": "Setubal", "lat": round(38.524398, 2), "lon": round(-8.888197, 2)},
    {"city": "Viseu", "lat": round(40.661014, 2), "lon": round(-7.909715, 2)},
    {"city": "Guarda", "lat": round(40.537328, 2), "lon": round(-7.267954, 2)},
    {"city": "Distrito+De+Santarem", "lat": round(39.236179, 2), "lon": round(-8.686806, 2)},
    {"city": "Castelo+Branco", "lat": round(39.822191, 2), "lon": round(-7.490869, 2)},
    {"city": "Viana+Do+Castelo", "lat": round(41.694599, 2), "lon": round(-8.830161, 2)},
    {"city": "Vila+Real", "lat": round(41.300620, 2), "lon": round(-7.744129, 2)},
    {"city": "Beja", "lat": round(38.015064, 2), "lon": round(-7.863227, 2)},
    {"city": "Braganca", "lat": round(41.805817, 2), "lon": round(-6.757189, 2)},
    {"city": "Portalegre", "lat": round(39.297590, 2), "lon": round(-7.430153, 2)},
    {"city": "Funchal", "lat": round(32.666817, 2), "lon": round(-16.924055, 2)},  # Madeira
    {"city": "Ponta+Delgada", "lat": round(37.741248, 2), "lon": round(-25.680790, 2)},  # Azores
    {"city": "teste", "lat": round(99, 2), "lon": round(99, 2)}
]

# Example of usage: print the rounded list
for city in cities_portugal:
    print(f"City: {city['city']}, Latitude: {city['lat']}, Longitude: {city['lon']}")
