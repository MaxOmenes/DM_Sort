import model.BasicSort as bs


class InsertionSort(bs.BasicSort):
    name = "Insertion"

    def __init__(self):
        super().__init__()

    def sort(self, arr):
        count = 0

        for i in range(1, len(arr)):

            key = arr[i]

            j = i - 1
            while j >= 0 and key < arr[j]:
                count += 1
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

        self.setTime(count)
