from model import Space
from view import ConsoleView

from math import cos, sin


class PlanetController:
    def __init__(self):
        self.space = Space()
        self.view = ConsoleView()

    def add_planet(self, name_of_planet, radius, speed, weight):
        if self.space.add_planets(name_of_planet, radius, speed, weight):
            self.view.show_message(f'планета {name_of_planet} добавлено!')
        else:
            self.view.show_message(f'Планета {name_of_planet} уже существует!')

    def show_planet(self):
        planets = self.space._planets
        self.view.display_planet(planets)
        for value in self.space._planets.values():
            parameters = value.parameters
            self.view.display_parameters_planet(parameters)

    def remove_planet(self, name):
        if self.space.remove_planet(name):
            self.view.show_message('Планета успешно удалено!')
        else:
            self.view.show_message('Такая планета не сущесвуеть!!')


    def run_simulation(self, name, number_of_steps, time_step):
        if name not in self.space._planets:
            self.view.show_message(f'Планета "{name}" не найдена')
            return

        planet = self.space._planets[name]

        try:
            angular_velocity = planet.rotation_speed / planet.radius_of_the_orbit
        except ZeroDivisionError:
            self.view.show_message('Радиус орбиты не может быть нулевым')
            return

        for step in range(1, number_of_steps + 1):
            angle = angular_velocity * step * time_step
            x = planet.radius_of_the_orbit * cos(angle)
            y = planet.radius_of_the_orbit * sin(angle)
            self.view.show_message(f'Шаг {step}: Планета "{name}" на позиции x={x:.2f}, y={y:.2f}')





