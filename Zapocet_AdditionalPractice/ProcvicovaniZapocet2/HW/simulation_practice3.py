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
    internet_q = deque(range(people_number))
    standard_q = deque()
    vip_q = deque()
    resolved_q = deque()

    queues_to_observe = [
        ("Internet",internet_q),
        ("Standard",standard_q),
        ("VIP",vip_q),
        ("Resolved",resolved_q),
    ]

    website_m = 20
    work_m = 40
    total_time_open = 0
    max_time_open = 86400

    Workers = [
        Worker("Generator",internet_q,None,website_m),
        Worker("Tech1",None,resolved_q,work_m),
        Worker("Tech2",None,resolved_q,work_m),
        Worker("Tech3",None,resolved_q,work_m)
    ]
    while total_time_open<=max_time_open:
        total_time_open+=1
        if total_time_open%60==0:
            print_snapshot(total_time_open,queues_to_observe)
        for worker in Workers:
            if worker.name=="Generator" and worker.timer ==0:
                r = random.randint(1,100)
                if r<=80:
                    worker.dest=standard_q
                else:
                    worker.dest=vip_q
            else:
                if len(vip_q)==0 and worker.timer==0:
                    worker.source=standard_q
                elif worker.timer==0:
                    worker.source=vip_q
            worker_tick(worker)

if __name__ == "__main__":
    main()