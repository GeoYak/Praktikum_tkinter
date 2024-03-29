import time
def partition(data, head, tail, drawData, tick):
    border = head
    pivot = data[tail]
    drawData(data, getColor(len(data), head, tail, border, border))
    time.sleep(tick)
    for j in range(head, tail):
        if data[j] < pivot:

            drawData(data, getColor(len(data), head, tail, border, j, True))
            time.sleep(tick)

            data[border], data[j] = data[j], data[border]
            border += 1

        drawData(data, getColor(len(data), head, tail, border, j))
        time.sleep(tick)

    drawData(data, getColor(len(data), head, tail, border, tail, True))
    time.sleep(tick)
    data[border], data[tail] = data[tail], data[border]
    return border


def quick_sort(data, head, tail, drawData, tick):
    if head < tail:
        partitionIdx = partition(data, head, tail, drawData, tick)
        #Левая часть
        quick_sort(data, head, partitionIdx-1, drawData, tick)
        #Правая часть
        quick_sort(data, partitionIdx+1, tail, drawData, tick)

def getColor(dataLen, head, tail, border, currIdx, isSwaping = False):
    colorArray = []
    for i in range(dataLen):
        if i >= head and i <= tail:
            colorArray.append('gray')
        else:
            colorArray.append('white')
        if i == tail:
            colorArray[i] = 'blue'
        elif i == border:
            colorArray[i] = 'red'
        elif i == currIdx:
            colorArray[i] = 'yellow'
        if isSwaping:
            if i == border or i == currIdx:
                colorArray[i] = 'green'
    return colorArray
