def gradeFilter(grades: list[int]) -> list:
    newScores = []
    for n in grades:
        if n>50:
            newScores.append(n)
    return newScores

def averageGrades(filteredGrades: list[int]) -> float:
    scores = 0
    count = 0
    for n in filteredGrades:
        scores+=n
        count+=1
    return(scores/count)


def main():
    grades = [45, 88, 51, 12, 99, 49, 60]
    print(f"Passing scores: {gradeFilter(grades)} and the average score is: {averageGrades(gradeFilter(grades))}")

if __name__ == '__main__':
    main()