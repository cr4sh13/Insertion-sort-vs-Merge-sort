import Sorting
import random
import matplotlib.pyplot as plt
from timeit import default_timer as timer


# crea un vettore random da n elementi
def randomList(n):
    A = []
    for i in range(n):
        A.append(i)
    random.shuffle(A)
    return A


# crea un vettore ordinato da n elementi
def orderList(n):
    A = []
    for i in range(n):
        A.append(i)
    return A


# esegue 10 iterazioni su un vettore da n elementi e calcola la media dei tempi
def sortingTimeMedium(n, fileIns, fileMerge):
    insertionSortTime = []
    mergeSortTime = []

    for i in range(10):

        listIns = randomList(n)
        listMerge = randomList(n)

        # scrivo su file di testo i vettori su cui effettuare i test
        for j in range(n):
            fileIns.write("%d " % listIns[j])
            fileMerge.write("%d " % listMerge[j])

        start = timer()
        Sorting.insertionSort(listIns)
        end = timer()
        time = end - start
        fileIns.write("Tempo impiegato: %f \r\n" % time)
        insertionSortTime.append(time)

        start = timer()
        Sorting.mergeSort(listMerge, 0, len(listMerge) - 1)
        end = timer()
        time = end - start
        fileMerge.write("Tempo impiegato: %f \r\n" % time)
        mergeSortTime.append(time)

    # calcola la media dei tempi
    mediaInsertion = 0
    for k in range(len(insertionSortTime)):
        mediaInsertion += insertionSortTime[k]
    mediaInsertion = mediaInsertion / 10

    mediaMerge = 0
    for k in range(len(mergeSortTime)):
        mediaMerge += mergeSortTime[k]
    mediaMerge = mediaMerge / 10

    return mediaInsertion, mediaMerge


# test insertion sort e merge sort caso medio
def testMediumCase():
    pltInsertionSort = []
    pltMergeSort = []
    X = []
    fileInsertion = open("DatiTest/InsertionSortMediumCase.txt", "w")
    fileMerge = open("DatiTest/MergeSortMediumCase.txt", "w")
    fileTable = open("DatiTest/TempiCasoMedio.txt", "w")
    n = 100

    while n <= 5000:
        mediaInsertionSort, mediaMergeSort = sortingTimeMedium(n, fileInsertion, fileMerge)
        fileTable.write("%d " % n)
        fileTable.write("InsertionSort %f " % mediaInsertionSort)
        fileTable.write("MergeSort %f " % mediaMergeSort)
        fileTable.write("\n")
        pltInsertionSort.append(mediaInsertionSort)
        pltMergeSort.append(mediaMergeSort)
        X.append(n)
        n += 100

    fileInsertion.close()
    fileMerge.close()
    fileTable.close()

    plt.figure()
    plt.plot(X, pltInsertionSort, 'r', label='Insertion sort')
    plt.plot(X, pltMergeSort, 'b', label='Merge sort')
    plt.xlabel("Numero elementi da ordinare")
    plt.ylabel("Tempo impiegato (s)")
    plt.legend(loc='upper left')
    plt.show()


# esegue 10 iterazioni su un vettore da n elementi e calcola la media dei tempi
def sortingTimeOrder(n, fileIns, fileMerge):
    insertionSortTime = []
    mergeSortTime = []

    for i in range(10):

        listIns = orderList(n)
        listMerge = orderList(n)

        # scrivo su file di testo i vettori su cui effettuare i test
        for j in range(n):
            fileIns.write("%d " % listIns[j])
            fileMerge.write("%d " % listMerge[j])

        start = timer()
        Sorting.insertionSort(listIns)
        end = timer()
        time = end - start
        fileIns.write("Tempo impiegato: %f \r\n" % time)
        insertionSortTime.append(time)

        start = timer()
        Sorting.mergeSort(listMerge, 0, len(listMerge) - 1)
        end = timer()
        time = end - start
        fileMerge.write("Tempo impiegato: %f \r\n" % time)
        mergeSortTime.append(time)

    # calcola la media dei tempi
    mediaInsertion = 0
    for k in range(len(insertionSortTime)):
        mediaInsertion += insertionSortTime[k]
    mediaInsertion = mediaInsertion / 10

    mediaMerge = 0
    for k in range(len(mergeSortTime)):
        mediaMerge += mergeSortTime[k]
    mediaMerge = mediaMerge / 10

    return mediaInsertion, mediaMerge


# test insertion sort e merge sort caso vettore ordinato
def testOrderCase():
    pltInsertionSort = []
    pltMergeSort = []
    X = []
    fileInsertion = open("DatiTest/InsertionSortOrderCase.txt", "w")
    fileMerge = open("DatiTest/MergeSortOrderCase.txt", "w")
    fileTable = open("DatiTest/TempiCasoVettoreOrdinato.txt", "w")
    n = 100

    while n <= 5000:
        mediaInsertionSort, mediaMergeSort = sortingTimeOrder(n, fileInsertion, fileMerge)
        fileTable.write("%d " % n)
        fileTable.write("InsertionSort %f " % mediaInsertionSort)
        fileTable.write("MergeSort %f " % mediaMergeSort)
        fileTable.write("\n")
        pltInsertionSort.append(mediaInsertionSort)
        pltMergeSort.append(mediaMergeSort)
        X.append(n)
        n += 100

    fileInsertion.close()
    fileMerge.close()
    fileTable.close()

    plt.figure()
    plt.plot(X, pltInsertionSort, 'r', label='Insertion sort')
    plt.plot(X, pltMergeSort, 'b', label='Merge sort')
    plt.xlabel("Numero elementi da ordinare")
    plt.ylabel("Tempo impiegato (s)")
    plt.legend(loc='upper left')
    plt.show()

# testMediumCase()
# testOrderCase()
