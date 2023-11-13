import model.InsertonSort as IS
import model.CocktailSort as CS
import model.ShellSort as SS
import model.QuickSort as QS


sorts = {IS.InsertionSort(),
         CS.CocktailSort(),
         SS.ShellSort(2),
         SS.ShellSort(3),
         QS.QuickSort()}

file_arr = open('input.txt', "r").read().split(",")
arr = [int(i) for i in file_arr]

output = open('output.txt', 'a')

for sort in sorts:
    sort.sort(arr.copy())
    output.write(sort.getName() + " sort: " +
                 str(sort.getAvgTime()) + "\n")

output.close()
