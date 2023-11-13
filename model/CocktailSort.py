import model.BasicSort as bs


class CocktailSort(bs.BasicSort):
    name = "Cocktail"

    def __init__(self):
        super().__init__()

    def sort(self, arr):
        count = 0

        n = len(arr)
        swapped = True
        start = 0
        end = n - 1

        while (swapped == True):
            swapped = False
            for i in range(start, end):
                if (arr[i] > arr[i + 1]):
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True
                    count += 1

            if (swapped == False):
                break

            swapped = False

            end = end - 1

            for i in range(end - 1, start - 1, -1):
                if (arr[i] > arr[i + 1]):
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True
                    count+=1

            start = start + 1

        self.setTime(count)