'''щас будем реализовать класс коньроллер который будет хранит в себе все необходимые данные и реализуем методы'''


class Planet:
    def __init__(self, name: str, radius: float, speed: float, weight: float):
        self.name = name
        self.radius_of_the_orbit = radius
        self.rotation_speed = speed
        self.weight = weight
        self.parameters = self.storing_parameters()

    def storing_parameters(self):
        return {
            'name': self.name,
            'radius': self.radius_of_the_orbit,
            'speed rotation': self.rotation_speed,
            'weight': self.weight
        }


class Space:
    def __init__(self):
        self._planets = {}

    def add_planets(self, name: str, radius: float, speed: float, weight: float):
        if name not in self._planets:
            self._planets[name] = Planet(name, radius, speed, weight)
            return True

    def remove_planet(self, name):
        if name in self._planets:
            del self._planets[name]
            return True

