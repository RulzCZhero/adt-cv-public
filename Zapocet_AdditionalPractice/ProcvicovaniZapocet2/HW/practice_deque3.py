from collections import deque

def simulate_bank(actions: list[tuple]):
    tellers={
        "A":deque(),
        "B":deque(),
        "C":deque()
    }

    for action,name,teller in actions:
        if action == "ARRIVE":
            tellers[teller].appendleft(name)
        if action == "SERVE" and len(tellers[teller])>0:
            tellers[teller].pop()
        if action == "TRANSFER" and len(tellers[teller])>0:
            tellers[teller].appendleft(tellers[name].popleft())
    
    for teller in tellers.values():
        print(teller)

def main():
    events = [
    ("ARRIVE", "Alice", "A"),
    ("ARRIVE", "Bob", "B"),
    ("ARRIVE", "Charlie", "A"),
    ("TRANSFER", "A", "B"), # Charlie moves from back of A to back of B
    ("SERVE", None, "B"),    # Bob is served
    ]
    simulate_bank(events)

if __name__ == "__main__":
    main()