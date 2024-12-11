from controller import PlanetController

def main():
    control = PlanetController()
    while True:
        control.view.display_menu()
        print()
        try:
            user_choice = control.view.get_input('Выберите действие: ')
            user_choice = int(user_choice)
            if user_choice < 1 or user_choice > 5:
                print('Не корректный выбор!')
            elif user_choice == 1:
                name_of_planet = control.view.get_input('Введите имя планеты: ')
                radius = float(control.view.get_input('Введите радиус орбиты: '))
                speed = float(control.view.get_input('Введите скорость вращения: '))
                weight = float(control.view.get_input('Введите массу планеты: '))
                control.add_planet(name_of_planet, radius, speed, weight)
            elif user_choice == 2:
                control.show_planet()
            elif user_choice == 3:
                name = control.view.get_input('Введите имя планеты:' )
                control.remove_planet(name)
            elif user_choice == 4:
                name = control.view.get_input('Введите имя планеты:')
                number_of_steps = int(control.view.get_input('Введите количество шагов симуляции: '))
                time_step = float(control.view.get_input('Введите временной шаг:'))
                control.run_simulation(name, number_of_steps, time_step)
            elif user_choice == 5:
                break
        except ValueError as e:
            print(e)


if __name__ == '__main__':
    main()





