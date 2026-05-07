import random
from collections import deque
from dataclasses import dataclass

@dataclass
class Worker:
    name: str
    source: deque
    dest: deque
    period: int
    spread_factor: float = 0.0
    timer: int = 0


def get_delay(period: int, spread_factor: float) -> int:
    return int(random.gauss(period, period * spread_factor))


def worker_tick(worker: Worker) -> None:
    if worker.timer>0:
        worker.timer-=1
    else:
        if len(worker.source)>0:
            worker.dest.append(worker.source.popleft())
            worker.timer = get_delay(worker.period,worker.spread_factor)



def print_snapshot(time: int, queues: list[tuple[str, deque]]) -> None:
    print(f"Čas: {time}")
    for name,q in queues:
        print(f"Fronta {name}: {len(q)}")


def main() -> None:
    people_number = 10000
    street_q = deque(range(people_number))
    ticket_q = deque()
    snack_q = deque()
    gate_q = deque()
    theater_q = deque()

    queues_to_observe = [
        ("Street",street_q),
        ("Ticket",ticket_q),
        ("Snack",snack_q),
        ("Gate",gate_q),
        ("Theater",theater_q),
    ]

    street_m = 20
    ticket_m = 25
    snack_m = 30
    gate_m = 5
    total_time_open = 0
    max_time_open = 86400

    Workers = [
        Worker("Generator",street_q,ticket_q,street_m),
        Worker("TicketAgent",ticket_q,snack_q,ticket_m),
        Worker("SnackMan",snack_q,gate_q,snack_m),
        Worker("TheaterGuy",gate_q,theater_q,gate_m)
    ]
    while total_time_open<=max_time_open:
        total_time_open+=1
        if total_time_open%60==0:
            print_snapshot(total_time_open,queues_to_observe)
        for worker in Workers:
            if(worker.name == "TicketAgent") and worker.timer == 0:
                r = random.randint(1,100)
                if r<=40:
                    worker.dest = snack_q
                else:
                    worker.dest = gate_q
            worker_tick(worker)

if __name__ == "__main__":
    main()