'''View -тображает список планет, параметры отдельной
планеты, анимацию движения (в виде текстового
описания, например, "Планета X завершила 1 полный
оборот")A'''


class ConsoleView:
    @staticmethod
    def display_menu():
        print('Команды:')
        print('1.Добавить планету: ')
        print('2.Показать планеты: ')
        print('3. Удалить планету: ')
        print('4. Запустить симуляцию: ')
        print('5. Выйти: ')

    @staticmethod
    def get_input(prompt):
        return input(prompt)

    @staticmethod
    def show_message(mess):
        print(mess)

    @staticmethod
    def display_planet(planets: dict):
        for planet in planets.values():
            print(planet.name)

    @staticmethod
    def display_parameters_planet(planet):
        for key, value in planet.items():
            print(f'{key}: {value}')







