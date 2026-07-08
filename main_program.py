"""
main_program.py
CS2410 Project 1
Author: Zuwairiyah Bari
-----------------------------------
Demonstrates:
    • Merge Sort (Task 1)
    • Rainfall Module usage (Task 2)
All rainfall outputs displayed in centimeters.
"""

import random
import rainfall_module as rm


# ----------------------------
# Task 1 – Merge Sort
# ----------------------------

def merge_sort(arr):
    """
    Sort a list of numbers using merge sort.
    """
    # Base case: if array has 0 or 1 element, it's already sorted
    if len(arr) <= 1:
        return arr

    # Find the middle point
    mid = len(arr) // 2

    # Split the array into two halves
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_sorted, right_sorted)


def merge(left, right):
    """
    Merge two sorted lists into one sorted list.
    """
    result = []
    i = 0  # Index for left list
    j = 0  # Index for right list

    # Compare elements from both lists and add smaller one to result
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add any remaining elements from left list
    while i < len(left):
        result.append(left[i])
        i += 1

    # Add any remaining elements from right list
    while j < len(right):
        result.append(right[j])
        j += 1

    return result


# ----------------------------
# Main Program
# ----------------------------

def main():
    print("=" * 60)
    print("CS2410 PROJECT 1")
    print("MERGE SORT & RAINFALL ANALYSIS")
    print("=" * 60)

    # Task 1: Merge Sort Demonstration
    print("\n*** TASK 1: MERGE SORT ***")

    # Generate random list of 10 integers
    original_list = [random.randint(1, 100) for _ in range(10)]
    print(f"Original list: {original_list}")

    # Sort using our merge sort
    sorted_list = merge_sort(original_list.copy())
    print(f"Sorted list:   {sorted_list}")

    # Verify with Python's built-in sort
    python_sorted = sorted(original_list)
    print(f"Python sorted: {python_sorted}")
    print(f"Merge sort correct: {sorted_list == python_sorted}")

    # Task 2: Rainfall Analysis
    print("\n*** TASK 2: RAINFALL ANALYSIS ***")
    print("-" * 40)

    # Get the rainfall data from our module
    data = rm.rainfall_data

    # Display the original data
    print("Monthly Rainfall Data:")
    for month, rainfall_in in data.items():
        month_name = rm.get_month_name(month)
        rainfall_cm = rm.inches_to_cm(rainfall_in)
        print(f"  {month_name:9s}: {rainfall_in:6.1f} in = {rainfall_cm:6.2f} cm")

    print("\n" + "-" * 40)
    print("ANALYSIS RESULTS:")
    print("-" * 40)

    # Use all the functions from our module
    try:
        # 1. Month with maximum precipitation
        max_month = rm.find_month_max_precipitation(data)
        max_rain_in = data[max_month]
        max_rain_cm = rm.inches_to_cm(max_rain_in)
        print(f"1. Maximum rainfall: {rm.get_month_name(max_month)}")
        print(f"   Amount: {max_rain_in:.1f} in = {max_rain_cm:.2f} cm")

        # 2. Month with minimum precipitation
        min_month = rm.find_month_min_precipitation(data)
        min_rain_in = data[min_month]
        min_rain_cm = rm.inches_to_cm(min_rain_in)
        print(f"2. Minimum rainfall: {rm.get_month_name(min_month)}")
        print(f"   Amount: {min_rain_in:.1f} in = {min_rain_cm:.2f} cm")

        # 3. Average precipitation
        avg_in = rm.calculate_average_precipitation(data)
        avg_cm = rm.inches_to_cm(avg_in)
        print(f"3. Average rainfall: {avg_in:.2f} in = {avg_cm:.2f} cm")

        # 4. Count months above average
        above_avg_count = rm.count_months_above_average(data)
        print(f"4. Months above average: {above_avg_count}")

        # 5. Months sorted by precipitation (descending)
        sorted_months = rm.bubble_sort_months_descending(data)
        print("5. Months sorted by rainfall (descending):")
        for i, (month, rainfall) in enumerate(sorted_months, 1):
            rain_cm = rm.inches_to_cm(rainfall)
            month_name = rm.get_month_name(month)
            print(f"   {i:2d}. {month_name:9s}: {rain_cm:6.2f} cm")

    except Exception as e:
        print(f"Error during rainfall analysis: {e}")

    print("\n" + "=" * 60)
    print("PROGRAM COMPLETED SUCCESSFULLY")
    print("=" * 60)


# Run the main function
if __name__ == "__main__":
    main()