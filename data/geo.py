import random

cities_canada = [
    {"City": "Toronto", "State": "Ontario", "Latitude": 43.65107, "Longitude": -79.347015, "Population": 2731571},
    {"City": "Montreal", "State": "Quebec", "Latitude": 45.5016889, "Longitude": -73.567256, "Population": 1704694 },
    {"City": "Vancouver", "State": "British Columbia", "Latitude": 49.2827291, "Longitude": -123.1207375, "Population": 631486},
    {"City": "Calgary", "State": "Alberta", "Latitude": 51.0499996, "Longitude": -114.0666666, "Population": 1239220},
    {"City": "Edmonton", "State": "Alberta", "Latitude": 53.5409441, "Longitude": -113.493797, "Population": 1062643},
    {"City": "Ottawa", "State": "Ontario", "Latitude": 45.421106, "Longitude": -75.690308, "Population": 934243},
    {"City": "Winnipeg", "State": "Manitoba", "Latitude": 49.895136, "Longitude": -97.1383744, "Population": 705244},
    {"City": "Quebec City", "State": "Quebec", "Latitude": 46.8138783, "Longitude": -71.2079809, "Population": 705103},
    {"City": "Hamilton", "State": "Ontario", "Latitude": 43.2560802, "Longitude": -79.872858, "Population": 693645},
    {"City": "Kitchener", "State": "Ontario", "Latitude": 43.4481957, "Longitude": -80.4809771, "Population": 470015},
    {"City": "London", "State": "Ontario", "Latitude": 42.9836747, "Longitude": -81.24959, "Population": 383822},
    {"City": "Victoria", "State": "British Columbia", "Latitude": 48.4283182, "Longitude": -123.3649533, "Population": 335696},
    {"City": "Halifax", "State": "Nova Scotia", "Latitude": 44.648618, "Longitude": -63.585948, "Population": 297943},
    {"City": "Oshawa", "State": "Ontario", "Latitude": 43.8975441, "Longitude": -78.8638746, "Population": 313858},
    {"City": "Windsor", "State": "Ontario", "Latitude": 42.3016496, "Longitude": -83.0307454, "Population": 233763},
    {"City": "Saskatoon", "State": "Saskatchewan", "Latitude": 52.1343694, "Longitude": -106.647656, "Population": 246376},
    {"City": "Regina", "State": "Saskatchewan", "Latitude": 50.4487609, "Longitude": -104.6173104, "Population": 215106},
    {"City": "Barrie", "State": "Ontario", "Latitude": 44.3893565, "Longitude": -79.690332, "Population": 141434},
    {"City": "St. John's", "State": "Newfoundland and Labrador", "Latitude": 47.5615, "Longitude": -52.7126, "Population": 108860},
    {"City": "Kelowna", "State": "British Columbia", "Latitude": 49.8884238, "Longitude": -119.4911912, "Population": 141767},
    {"City": "Sherbrooke", "State": "Quebec", "Latitude": 45.403753, "Longitude": -71.9384162, "Population": 161323},
    {"City": "Sudbury", "State": "Ontario", "Latitude": 46.49272, "Longitude": -80.991211, "Population": 164689},
    {"City": "Kingston", "State": "Ontario", "Latitude": 44.231172, "Longitude": -76.4859544, "Population": 136671},
    {"City": "Thunder Bay", "State": "Ontario", "Latitude": 48.3808951, "Longitude": -89.2476823, "Population": 107909},
    {"City": "Moncton", "State": "New Brunswick", "Latitude": 46.0878165, "Longitude": -64.7782313, "Population": 85341},
    {"City": "Saint John", "State": "New Brunswick", "Latitude": 45.2729557, "Longitude": -66.0676636, "Population": 67632},
    {"City": "Nanaimo", "State": "British Columbia", "Latitude": 49.1658843, "Longitude": -123.9400647, "Population": 104936},
    {"City": "Kamloops", "State": "British Columbia", "Latitude": 50.674522, "Longitude": -120.327267, "Population": 90280},
    {"City": "Fredericton", "State": "New Brunswick", "Latitude": 45.9635895, "Longitude": -66.6431153, "Population": 58249},
    {"City": "Chilliwack", "State": "British Columbia", "Latitude": 49.1579345, "Longitude": -121.9514666, "Population": 77936},
]


class Location:
    
    @staticmethod
    def random_location():
        # Calculate probabilities based on population
        total_population = sum(city["Population"] for city in cities_canada)
        probabilities = [city["Population"] / total_population for city in cities_canada]
        
        # Select a random city based on probabilities
        local = random.choices(cities_canada, probabilities)[0]
        return local
