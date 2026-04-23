import random
import matplotlib.pyplot as plt

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

def selection_sort(seznam_start):
    cisla = seznam_start.copy()
    c = len(cisla)

    for i in range(c):
        index_min = i

        for x in range(i + 1, c):
            if cisla[x] < cisla[index_min]:
                index_min = x

        cisla[i], cisla[index_min] = cisla[index_min], cisla[i]

    return cisla



def bubble_sort(seznam_start):
    cisla = seznam_start.copy()
    c = len(cisla)
    plt.ion()
    plt.show()

    for i in range(c):
        for j in range(c - i - 1):
            index_highlight1 = j
            index_highlight2 = j + 1
            colors = ["steelblue"] * len(cisla)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"
            plt.clf()
            plt.bar(range(len(cisla)), cisla, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.1)
            if cisla[j] > cisla[j + 1]:

                cisla[j], cisla[j + 1] = cisla[j + 1], cisla[j]
    plt.ioff()
    plt.show()
    return cisla

if __name__ == "__main__":
    values = random_numbers(10)
    print(f"začáteční seznam: {values}")
    print(f"seřazené selection sort: {selection_sort(values)}")
    print(f"seřazené bubble sort: {bubble_sort(values)}")


    test = [5, 1, 4, 2, 8]
    print(test)

    print(f"test selection sort: {selection_sort(test)}")
    print(f"test bubble sort: {bubble_sort(test)}")

    bubble = bubble_sort(random_numbers(10))
    print(bubble)
    # small = random_numbers(5, low=0, high=20)  # 5 čísel v rozsahu 0–20
    # print(selection_sort(random_numbers(14)))