'''
Tento program simuluje cestu autem z půjčovny.

- Auto je reprezentováno datovou třídou `Car` a je zpočátku půjčeno s prázdnou nádrží.
- Jednotlivé úseky cesty jsou reprezentovány datovou třídou `Trip`.
- Logika je implementována pomocí funkcí, nikoli metod třídy.

Implementujte chybějící části a opravte případné chyby.
Dodržujte signatury funkcí a názvy symbolů.
'''

from dataclasses import dataclass


@dataclass
class Trip:
    """
    Reprezentuje úsek cesty.

    Atributy:
        distance: Délka úseku cesty v km.
        fuel_consumption: Spotřeba paliva v litrech na 100 km.
    """
    distance: int
    fuel_consumption: float


@dataclass
class Car:
    """
    Datová struktura reprezentující auto.

    Atributy:
        owner: Jméno majitele auta.
        fuel_capacity: Maximální kapacita nádrže v litrech.
        fuel_level: Aktuální hladina paliva v litrech.
        distance_traveled: Celková ujetá vzdálenost v km od půjčení.
    """

    owner: str
    fuel_capacity: float
    fuel_level: float = 0.0
    distance_traveled: float = 0.0


def refuel(car: Car, amount: float) -> None:
    """
    Natankuje palivo do nádrže auta.

    - Záporné množství tankování je ignorováno.
    - Nádrž nelze přeplnit.
    """
    # TODO Ošetřete záporné tankování (nelze tankovat zaporne mnozstvi). 
    # TODO Doplňte palivo bez přeplnění nádrže: V takovem pripade se nadrz naplni na maximalni kapacitu.
    if amount<=0:
        return None
    if car.fuel_level+amount > car.fuel_capacity:
        car.fuel_level = car.fuel_capacity
    else:
        car.fuel_level+=amount


def print_car_state(car: Car) -> None:
    """Pomocná ladicí funkce."""
    print(f"fuel_level: {car.fuel_level:.2f} dist:{car.distance_traveled:.2f} km")


def simulate(car: Car, trips: list[Trip]) -> tuple[float, float]:
    """
    Simuluje seznam úseků cesty.

    Pokud auto dojde palivo během úseku, ujede pouze jeho část
    a simulace skončí.
    """

    # TODO Simulujte průjezd úseky, při nedostatku paliva vozidlo dale nepokracuje v jizde.
    for trip in trips:
        if car.fuel_level<=0:
            return car.distance_traveled, car.fuel_level
        tempFuel = car.fuel_level
        car.fuel_level-=(trip.distance/100)*trip.fuel_consumption
        if car.fuel_level<=0:
            car.fuel_level=0
            car.distance_traveled+=(trip.distance/trip.fuel_consumption)*tempFuel
        else:
            car.distance_traveled+=trip.distance

    return car.distance_traveled, car.fuel_level


def answer_query() -> tuple[float, float]:
    """
    Spustí celou simulaci a vrátí hladiny paliva po dvou sériích jízd.
    """

    trips_1 = [
        Trip(100, 7),
        Trip(200, 6),
        Trip(50, 9),
    ]
    trips_2 = [
        Trip(50, 2),
    ]

    car = Car("Petr", 50)

    # Simulujte celý proces:
    # 1. Vytvořte auto s 50l nádrží.
    # 2. Natankujte do plna -- pouzijte funkci refuel.
    # 3. Absolvujte první sérii jízd -- pouzijte funkci simulate.
    # 4. Natankujte 10 litrů -- pouzijte funkci refuel.
    # 5. Absolvujte druhou sérii jízd -- pouzijte funkci simulate.
    # Vraťte stav paliva po první a druhé sérii.
    refuel(car,50)
    fuel_after_first = simulate(car,trips_1)[1]
    refuel(car,10)
    fuel_after_second = simulate(car,trips_2)[1]
    return fuel_after_first, fuel_after_second


if __name__ == "__main__":
    print(answer_query())
