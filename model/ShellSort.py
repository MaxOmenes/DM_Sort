import model.BasicSort as bs


class ShellSort(bs.BasicSort):
    name = "Shell"
    h = 2  # default

    def __init__(self, h):
        super().__init__()
        self.h = h

    def getName(self):
        return self.name + " ("+str(self.h)+"h+1)"

    def sort(self, arr):
        count = 0

        gap = len(arr) // self.h - 1

        while gap > 0:
            j = gap
            while j < len(arr):
                i = j - gap

                while i >= 0:
                    count += 1
                    if arr[i + gap] > arr[i]:

                        break
                    else:
                        arr[i + gap], arr[i] = arr[i], arr[i + gap]

                    i = i - gap
                j += 1
            gap = gap // self.h - 1

        self.setTime(count)
