import random
from collections import deque
from dataclasses import dataclass


@dataclass
class Worker:
    name: str
    source: deque
    dest: list[deque]
    period: int
    spread_factor: float = 0.0
    timer: int = 0


def get_delay(period: int, spread_factor: float) -> int:
    return int(random.gauss(period, period * spread_factor))



def worker_tick(worker: Worker) -> None:
    worker.timer -=1
    delay=-1
    if worker.timer==0 and len(worker.source) != 0 and worker.name != "gate_keeper":
        worker.dest[0].append(worker.source.pop())

    if worker.timer==0 and len(worker.source) != 0 and worker.name == "gate_keeper":
        fronts_count = len(worker.dest)
        person = worker.source.pop()
        worker.dest[person%fronts_count].append(person)
        #for n in range(1,fronts_count+1):
          #  if person%n==0:
         #       worker.dest[n-1].append(person)
        #       continue

    if worker.timer<0:
        while delay < 0:
            delay = get_delay(worker.period,worker.spread_factor)
        print(f"Worker bude pracovat po {delay}")
        worker.timer = delay



def print_snapshot(time: int, queues: list[tuple[str, deque]]) -> None:
    info_string = ""
    for q_name,q in queues:
        info_string+=(f"\t{q_name} : {len(q)}\n")
    print(f"cas: {time}\n{info_string}")    


def main() -> None:
    people_number = 1000000
    people_in_the_city = deque(list(range(people_number)))

    
    # 1. Vytvoření front
    vege_q = deque ([])
    frui_q = deque ([])
    meat_q = deque ([])
    final_q = deque ([])
    rip_q = deque ([])

    # Seznam pro výpis (jméno, fronta)
    queues_to_observe = [
        ("city",people_in_the_city),
        ("vege",vege_q),
        ("frui",frui_q),
        ("meat",meat_q),
        ("final",final_q),
        ("rip",rip_q)
    ]

    # Parametry simulace (střední hodnoty časů v sekundách)
    day_m = 30  # Každých 30s přijde někdo z ulice
    gate_m = 15  # Gate keeper každého odbavuje 5s
    vege_m = 45  # Vážení zeleniny trvá 45s
    frui_m = 45
    meat_m = 45
    final_m = 2 * 60  # Pokladna zabere 2 minuty

    # 2. Vytvoření pracovníků (Worker)
    # Worker(jméno, zdroj, cíl, perioda, spread_factor)
    workers = [
     Worker("gate_keeper",people_in_the_city,[vege_q,frui_q,meat_q],day_m,1),
     Worker("vege",vege_q,[final_q],vege_m,1),
     Worker("frui",frui_q,[final_q],frui_m,1),
     Worker("meat",meat_q,[final_q],meat_m,1),
     Worker("final",final_q,[rip_q],final_m,1),
     Worker("final",final_q,[rip_q],final_m,1),
     Worker("final",final_q,[rip_q],final_m,1),
     Worker("final",final_q,[rip_q],final_m,1)
    ]
    # 3. Hlavní smyčka simulace
    max_time = 3600*24
    for s in range(max_time):
        for worker in workers:
            worker_tick(worker)
        print_snapshot(s,queues_to_observe)
if __name__ == "__main__":
    main()
