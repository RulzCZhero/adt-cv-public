from collections import deque

def manage_checkout_line(actions:list[tuple]) -> list:
    que = deque()
    for action,name in actions:
        if action == "ARRIVE":
            que.appendleft(name)
        if action == "VIP":
            que.append(name)
        if action == "SERVE":
            que.pop()
        if action == "CLOSE":
            que.popleft()
    currentList = list(que)
    return currentList
        

def main():
    events = [
    ("ARRIVE", "Alice"),
    ("ARRIVE", "Bob"),
    ("VIP", "Charlie"),   # Charlie goes to the front
    ("SERVE", None),      # Charlie is served
    ("ARRIVE", "David"),
    ("CLOSE", None)       # David is told to leave
]
    idk = manage_checkout_line(events)
    for n in idk:
        print(n)


if __name__ == "__main__":
    main()