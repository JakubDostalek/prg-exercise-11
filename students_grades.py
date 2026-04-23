from sorting import random_numbers
class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)


    def get_grade(self, index):
        body = self.get_by_index(index)

        if body >= 90:
            return "A"
        elif body >= 80:
            return "B"
        elif body >= 70:
            return "C"
        elif body >= 60:
            return "D"
        elif body >= 50:
            return "E"
        else:
            return "F"


    def find(self,konkretni_body):
        indexy = []

        for i in range(self.count()):
            if self.scores[i] == konkretni_body:
                indexy.append(i)

        return indexy


    def get_sorted(self):

        cisla = self.scores[:]
        c = len(cisla)

        for i in range(c):
            for j in range(c - i - 1):

                if cisla[j] > cisla[j + 1]:
                    cisla[j], cisla[j + 1] = cisla[j + 1], cisla[j]

        return cisla

if __name__ == "__main__":
    # results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    #
    # print(results.count())  # 9
    # print(results.get_by_index(2))  # 91
    # print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]
    # print("__________")
    # print(results.get_grade(2))  # A (91 bodů)
    # print(results.get_grade(6))  # A (100 bodů)
    # print(results.get_grade(7))  # F (38 bodů)
    # print("__________")
    # print(results.find(100))  # [6]
    # print(results.find(50))  # [4]
    # print(results.find(77))  # []
    # print("__________")
    # print(results.get_sorted())  # [38, 42, 50, 58, 67, 73, 85, 91, 100]
    # print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]  ← beze změny

    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

    print(f"Počet studentů: {results.count()}\n" + "-" * 20)

    for i in range(results.count()):
        print(f"Student {i}: {results.get_by_index(i)} points - {results.get_grade(i)}")

    print(f"{'-' * 20}\nIndexy se 100 body: {results.find(100)}")
    print(f"Seřazené výsledky: {results.get_sorted()}\n" + "-" * 20)

    rand_res = StudentsGrades(random_numbers(30, 0, 100))
    print(f"Náhodných studentů: {rand_res.count()}")
    print(f"Seřazené náhodné: {rand_res.get_sorted()}")