from collections import deque

def process_scores(new_scores: list[int]):
    scores = deque(maxlen=4)   
    for n in new_scores:
        scores.append(n)
        if sum(scores)/len(scores) <50:
            print("ALERT: System unstable! Current avg: [average]")
        else:
            print(f"System OK. Last 4: {scores}")
def main():
    scores = [80, 90, 70, 20, 30, 40, 90]
    process_scores(scores)

if __name__ == "__main__":
    main()