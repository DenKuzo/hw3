class SuperHero:
    people = 'peolpe'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def run(self):
        print(f'{self.name} is running')

    def health_point(self):
        print(f'Здоровье героя {self.health_points * 2} хп')

    def __str__(self):
        return f'{self.nickname} {self.superpower} {self.health_points}'

    def __len__(self):
        return f'{len(self.catchphrase)}'


hero = SuperHero('Piter', 'Spider-man', 'spiderweb', 1000, 'Чем больше сила тем больше ответсвенности')


# print(hero)
# hero.health_point()
# hero.run()
# print(f'длина фразы героя {hero.__len__()} букв')


class Legend(SuperHero):
    people = 'people'

    def __init__(self, name, nickname, superpower, health_point, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_point, catchphrase)

        self.damage = damage
        self.fly = fly

    def legend_damage(self):
        print(f'Урон героя {self.damage}')

    def double_healthpoints(self):
        print(f'Здоровье героя {self.health_points ** 2} хп')
        self.fly = True

    def fly_sky(self):
        print(f'fly in the {self.name}_phrase')


class AirHero(Legend):
    air = 'air'

    def double_healthpoints(self):
        print(f'Здоровье героя{self.health_points}хп')
        self.fly = True

    def fly_sky(self):
        print(f'fli in the{self.fly}_phrase')


thor = Legend('thor', 'bog', 'grom', 200, 'я бог грома', damage=300)
air_hero = AirHero('Volodya', 'Valir', 'Flame', 1000, 'Почувствуй мое пламя', damage=200)
print(thor.name, thor.nickname, thor.superpower)
thor.fly_sky()
thor.double_healthpoints()
print(thor.catchphrase)
print(thor.damage)

print(air_hero.name, air_hero.nickname, air_hero.superpower)
air_hero.fly_sky()
air_hero.double_healthpoints()
print(air_hero.catchphrase)
print(air_hero.damage)




class Villian(Legend):
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        super().__init__(self, name, nickname, superpower, health_points, catchphrase)
        SuperHero.people = 'monster'

    def gen_x(self):
        pass

def crit(hero):
    return hero.damage ** 2

ninja = Villian('Hanzo', 'Salamandra', 'Ninja', 2000, 'Больше крови и плоти!')
print(ninja.name)
print(crit(thor))
print(crit(air_hero))