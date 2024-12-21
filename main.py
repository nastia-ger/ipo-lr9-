from collision import isCorrectRect, isCollisionRect, intersectionAreaRect, intersectionAreaMultiRect

rectangles = [
    [(-3, 1), (9, 10)],
    [(-7, 0), (13, 12)],
    [(0, 0), (5, 5)],
    [(2, 2), (7, 7)]
]

for rect in rectangles:
    print(f"isCorrectRect({rect}): {isCorrectRect(rect)}")

for i in range(len(rectangles)):
    rect1 = rectangles[i]
    for j in range(i + 1, len(rectangles)):
        rect2 = rectangles[j]
        print(f"isCollisionRect({rect1}, {rect2}): {isCollisionRect(rect1, rect2)}")

for i in range(len(rectangles)):
    rect1 = rectangles[i]
    for j in range(i + 1, len(rectangles)):
        rect2 = rectangles[j]
        print(f"intersectionAreaRect({rect1}, {rect2}): {intersectionAreaRect(rect1, rect2)}")

print(f"intersectionAreaMultiRect(rectangles): {intersectionAreaMultiRect(rectangles)}")