def minimum(array):
    if len(array) == 0:
        return -1

    min_value = array[0]
    for i in range(len(array)):
        if array[i] < min_value:
            min_value = array[i]
    return min_value


def average(array):
  summ = 0
  for x in array:
    summ += x
  return summ / len(array)


def main():
    arr = [34, 553, 11, 84, 7, 506, 202]
    print(minimum(arr))
    print(average(arr))


main()