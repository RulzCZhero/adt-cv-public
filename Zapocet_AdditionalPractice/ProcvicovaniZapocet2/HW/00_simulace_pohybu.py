def simulate(accelerations: list[tuple[int, float]]) -> tuple[list[float], list[float]]:
    """
    Simuluje pohyb s časovým krokem 1 sekunda.
    """
    distance = 0.0
    speed = 0.0
    speeds = []
    distances = []
    
    for duration, accelerate in accelerations:
        for n in range(duration):
            speed += accelerate
            distance += speed
            speeds.append(speed)
            distances.append(distance)
            
    return speeds, distances


def simulate_with_step(accelerations: list[tuple[int, float]], step: float) -> tuple[list[float], list[float], list[float]]:
    """
    Simuluje pohyb s nastavitelným časovým krokem.
    """
    distance = 0.0
    speed = 0.0
    total_time = 0.0 
    
    speeds = []
    distances = []
    timestamps = []
    
    for duration, accelerate in accelerations:
        current_segment_time = 0.0
        while current_segment_time < duration:
            speed += accelerate * step
            distance += speed * step
            total_time += step
            current_segment_time += step
            speeds.append(speed)
            distances.append(distance)
            timestamps.append(total_time)
            
    return speeds, distances, timestamps

# Příklad použití pro lokální testování (nebude hodnoceno)

accelerations_data = [(20, 0.5), (1, -5), (10, 2)]
speeds1, distances1 = simulate(accelerations_data)
print("Výsledky `simulate`:")
print(f"  Konečná rychlost: {speeds1[-1] if speeds1 else 0:.2f} m/s")
print(f"  Celková vzdálenost: {distances1[-1] if distances1 else 0:.2f} m")
time_step = 0.1
speeds2, distances2, timestamps2 = simulate_with_step(accelerations_data, time_step)
print(f"\nVýsledky `simulate_with_step` (krok={time_step}s):")
print(f"  Konečná rychlost: {speeds2[-1] if speeds2 else 0:.2f} m/s")
print(f"  Celková vzdálenost: {distances2[-1] if distances2 else 0:.2f} m")