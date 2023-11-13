import model.BasicSort as bs


class QuickSort(bs.BasicSort):
    name = "Quick"
    count = 0

    def __init__(self):
        super().__init__()

    def sort(self, arr):
        self.quicksort(arr, 0, len(arr)-1)

    def partition(self, array, low, high):
        pivot = array[high]

        i = low - 1

        for j in range(low, high):
            self.count += 1
            if array[j] <= pivot:
                i = i + 1
                (array[i], array[j]) = (array[j], array[i])

        (array[i + 1], array[high]) = (array[high], array[i + 1])

        return i + 1

    def quicksort(self, array, low, high):
        if low < high:
            pi = self.partition(array, low, high)

            self.quicksort(array, low, pi - 1)

            self.quicksort(array, pi + 1, high)

        self.setTime(self.count)
