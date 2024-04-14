import tkinter as tk
import random 
import time
import matplotlib.pyplot as plt
import numpy as np 

def insertion_sort(arr):
    """
    Sorts the given array using the insertion sort algorithm.
    This algorithm iterates over the array, starting from the second element.
    For each element, it 'inserts' the element into its correct position in the array.
    Shifts the larger elements to the right to make space for the current element.

    Args:
        arr: The array to be sorted
    
    Returns:
        arr: The sorted array
    """
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key
    return arr

def merge(arr1, arr2):
    """
    Merges two arrays into a single array in sorted order.
    Compares the smallest elements from each array and appends the smaller 
    one to the merged array. Continues this process until one of the arrays is empty.

    Args:
        arr1: The first array to be merged
        arr2: The second array to be merged
    
    Returns:   
        merged_arr: The merged array
    """
    merged_arr = []
    while len(arr1) > 0  and len(arr2) > 0:
        if arr1[0] > arr2[0]:
            merged_arr.append(arr2[0])
            arr2.pop(0)
        else:
            merged_arr.append(arr1[0])
            arr1.pop(0)
    while len(arr1) > 0:
        merged_arr.append(arr1[0])
        arr1.pop(0)
    while len(arr2) > 0:
        merged_arr.append(arr2[0])
        arr2.pop(0)
    return merged_arr

def merge_sort(arr):
    """
    Sorts the given array using the merge sort algorithm.
    Merge sort is a recursive divide and conquer algorithm that divides the array
    into two halves, sorts the two halves, and then merges the sorted halves.    
    Args:
        arr: The array to be sorted
    
    Returns:
        arr: The sorted array
    """
    if (len(arr) == 1):
        return arr
    l1 = arr[:len(arr)//2]
    l2 = arr[len(arr)//2:]

    l1 = merge_sort(l1)
    l2 = merge_sort(l2)
    return merge(l1, l2)

def selection_sort(arr):
    """
    Sorts the given array using the selection sort algorithm.
    Repeatedly selects the smallest element from the unsorted array and
    places it at the leftmost position of the unsorted array one element at a time.    
    Args:
        arr: The array to be sorted
    
    Returns:
        arr: The sorted array
    """
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr 

def bubble_sort(arr):
    """
    Sorts the given array using the bubble sort algorithm.
    Repeatedly compares adjacent elements and swaps them if 
    they are in the wrong order. 

    Args:
        arr: The array to be sorted
    
    Returns:
        arr: The sorted array
    """
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def partition_regular(arr, low, high):
    """
    Partitions the given array around the pivot element in this case the last element.

    Moves all elements less than the pivot to the left of the pivot and all elements greater than the pivot to the right.

    Args:
        arr: The array to be partitioned
        low: The starting index of the array
        high: The ending index of the array
    
    Returns:
        i+1: The index of the pivot element
    """
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def quick_sort_regular(arr, low, high):
    """
    Recuriesly sorts the given array using the quick sort algorithm.

    Partitions the array around a pivot element and recurisvely sorts the left and right subarrays.

    Args:
        arr: The array to be sorted
        low: The starting index of the array
        high: The ending index of the array
    
    Returns:
        arr: The sorted array
    """
    if low < high:
        pi = partition_regular(arr, low, high)
        quick_sort_regular(arr, low, pi-1)
        quick_sort_regular(arr, pi+1, high)
    return arr

def median_of_three(arr, low, high):
    """
    Chooses median of first, middle and last elements of array as pivot element.

    Improves the performance of quick sort by selecting a pivot element that is closer to the median of the array.

    Args:
        arr: The array to be sorted
        low: The starting index of the array
        high: The ending index of the array
    
    Returns:
       arr[high-1]: The pivot element
    """
    mid = (low + high) // 2
    if arr[mid] < arr[low]:
        arr[mid], arr[low] = arr[low], arr[mid]
    if arr[high] < arr[low]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[high] < arr[mid]:
        arr[mid], arr[high] = arr[high], arr[mid]
    arr[mid], arr[high-1] = arr[high-1], arr[mid]
    return arr[high-1]

def partition_median(arr, low, high):
    """
    Partitions the given array around the pivot element in this case the median of three elements.

    Moves all elements less than the pivot to the left of the pivot and all elements greater than the pivot to the right.
    Args:
        arr: The array to be partitioned
        low: The starting index of the array
        high: The ending index of the array
    
    Returns:
        Left: The index of the pivot element
    """
    pivot = median_of_three(arr, low, high)
    left = low + 1
    right = high - 2
    while True: 
        while arr[left] < pivot:
            left = left + 1
        while arr[right] > pivot:
            right = right - 1
        if left >= right:
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left = left + 1
            right = right - 1
    arr[left], arr[high-1] = arr[high-1], arr[left]
    return left

def quick_sort_median(arr, low, high):
    """
    Recuriesly sorts the given array using the quick sort algorithm with the median of three pivot element.

    Partitions the array around a pivot element and recurisvely sorts the left and right subarrays.

    Args:
        arr: The array to be sorted
        low: The starting index of the array
        high: The ending index of the array
    
    Returns:
        arr: The sorted array
    """
    if high <= low:
        return
    if high - low > 1:
        pi = partition_median(arr, low, high)
        quick_sort_median(arr, low, pi-1)
        quick_sort_median(arr, pi+1, high)
    else:
        if arr[high] < arr[low]:
            arr[low], arr[high] = arr[high], arr[low]
    return arr


def build_heap(arr, n):
    """
    Transforms array into max heap. A max heap is a complete binary tree that satisfies the heap property. 
    The heap property states that the parent node must be greater than or equal to its child nodes.  
    Iterates over the array starting from the last non-leaf node and heapifies the array.

    Args:
        arr: The array to be converted into a heap
        n: The size of the array
    
    Returns:
        arr: The heapified array
    """
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    return arr
    
def heapify(arr, n, i):
    """
    Ensures the heap property is maintained at a given node and recursively corrects the heap property if violated.

    Compares the parent node with its child nodes and swaps the parent node with the largest child node if the parent node is smaller.

    Args:
        arr: The array to be heapified
        n: The size of the array
        i: The index of the root node
    
    returns:
        arr: The heapified array
    """
    max = i 
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[max]:
        max = left
    
    if right < n  and arr[right] > arr[max]:
        max = right
    
    if max != i:
        arr[i], arr[max] = arr[max], arr[i]
        heapify(arr, n, max)
    return arr

def heapsort(arr):
    """
    Sorts the given array using the heap sort algorithm.
    By converting the array into a heap and then repeatedly removing the root node and heapifying the array.
    
    Args:
        arr: The array to be sorted
    
    Returns:
        arr: The sorted array
    """
    n = len(arr)
    build_heap(arr, n )
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr,i, 0)
    return arr

def plot_results(results, size):
    """
    Plots the running time of the selected algorithms for the given array size. Scaled to log scale to show the differences in running time.
    
    Args:
        results: A dictionary containing the running time of the selected algorithms
        size: The size of the array used for sorting
    """
    algorithms = list(results.keys())
    times = [results[alg] for alg in algorithms]

    fig, ax = plt.subplots(figsize=(10, 5))
    bars = ax.bar(algorithms, times, width=0.4, color='blue')  

    ax.set_xlabel("Algorithms")
    ax.set_xticks(range(len(algorithms)), algorithms, rotation=45, ha="right")
    ax.set_ylabel("Running Time (seconds)")
    ax.set_title(f'Algorithm Running Time Comparison for Array Size: {size}')
    ax.set_yscale('log')

    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2.0, height, f'{height:.2e}', ha='center', va='bottom')

    plt.tight_layout()
    plt.show()

def write_arr_to_file(arr, filename):
    """
    Writes the unsorted and sorted arrays to a file relating to its algorithm.

    Args:
        arr: The array to be written to the file
        filename: The name of the file to write the array to
    
    Returns:
        No return value 
    """
    with open(filename, 'w') as f:
        for num in arr:
            f.write(f"{num}\n")

def perform_sort():
    """
    Performs the sorting of the array based on the selected algorithm(s) and displays the results in the GUI.

    Args:
        No arguments
    
    Returns:
        No return value
    """

    size = int(size_entry.get())
    selections = algo_listbox.curselection()
    results = {}

    arr = [random.randint(0, 10000) for _ in range(size)]
    write_arr_to_file(arr, f"unsorted_array_{size}.txt")
    for i in selections:
        alg = algo_options[i]
        arr_copy = arr.copy()
        start_time = time.perf_counter()

        if alg == "Insertion Sort":
            sorted_arr = insertion_sort(arr_copy)
        elif alg == "Merge Sort":
            sorted_arr = merge_sort(arr_copy)
        elif alg == "Selection Sort":
            sorted_arr = selection_sort(arr_copy)
        elif alg == "Bubble Sort":
            sorted_arr = bubble_sort(arr_copy)
        elif alg == "Quick Sort Regular":
            sorted_arr = quick_sort_regular(arr_copy, 0, len(arr)-1)
        elif alg == "Quick Sort Median":
            sorted_arr = quick_sort_median(arr_copy, 0, len(arr)-1)
        elif alg == "Heap Sort":
            sorted_arr = heapsort(arr_copy)
        end_time = time.perf_counter()
        results[alg] = (end_time - start_time)

        write_arr_to_file(sorted_arr, f"{alg}_sorted_array_{size}.txt")
    plot_results(results, size)

# Initialize the GUI
root = tk.Tk()
root.title("Sorting Algorithms")
root.geometry('500x300')

# The GUI elements for selecting the algorithm and array size
algo_var = tk.StringVar()
algo_options = ["Insertion Sort", "Merge Sort", "Selection Sort", "Bubble Sort", "Quick Sort Regular", "Quick Sort Median", "Heap Sort"]
algo_var.set(algo_options[0])
algo_label = tk.Label(root, text="Select Algorithm(s): ")
algo_label.pack()
algo_listbox = tk.Listbox(root, selectmode = 'multiple', exportselection=0, width = 50, height = 7, font=('Helvetica', 12))

# Add the algorithm options to the listbox
for option in algo_options:
    algo_listbox.insert(tk.END, option)
algo_listbox.pack()

# Add the array size entry field and the sort button
size_label = tk.Label(root, text="Enter the array size: ")
size_label.pack()
size_entry = tk.Entry(root, width=20, font=('Helvetica', 12))
size_entry.pack()

# Add the sort button and the runtime label
sort_button = tk.Button(root, text="Sort", command=perform_sort)
sort_button.pack()

# Add the label to display the runtime of the selected algorithm
runtime_var = tk.StringVar()
runtime_label = tk.Label(root, textvariable=runtime_var)
runtime_label.pack()
root.mainloop()