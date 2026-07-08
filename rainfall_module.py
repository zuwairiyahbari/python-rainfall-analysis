"""
rainfall_module.py
CS2410 Project 1 - Rainfall Analysis Module
Author: Zuwairiyah Bari
-----------------------------------
This module provides functions to analyze monthly rainfall data.
All measurements are stored in inches but can be converted to centimeters.
"""

# Rainfall data for 2018 (month: rainfall in inches)
rainfall_data = {
    '01': 133.5, '02': 64.3, '03': 104.4, '04': 86.3,
    '05': 48.5, '06': 35.4, '07': 55.3, '08': 84.9,
    '09': 104.5, '10': 104.4, '11': 122.6, '12': 119.5
}

def find_month_max_precipitation(rainfall_dict):
    """
    Find the month with the maximum precipitation.

    Args:
        rainfall_dict (dict): Dictionary with month numbers as keys and rainfall in inches as values

    Returns:
        str: Month number with maximum precipitation
    """
    if not rainfall_dict:
        return None

    max_month = None
    max_rainfall = -9999

    # Loop through all months to find maximum
    for month, rainfall in rainfall_dict.items():
        if rainfall > max_rainfall:
            max_rainfall = rainfall
            max_month = month

    return max_month

def find_month_min_precipitation(rainfall_dict):
    """
    Find the month with the minimum precipitation.

    Args:
        rainfall_dict (dict): Dictionary with month numbers as keys and rainfall in inches as values

    Returns:
        str: Month number with minimum precipitation
    """
    if not rainfall_dict:
        return None

    min_month = None
    min_rainfall = 9999

    # Loop through all months to find minimum
    for month, rainfall in rainfall_dict.items():
        if rainfall < min_rainfall:
            min_rainfall = rainfall
            min_month = month

    return min_month

def calculate_average_precipitation(rainfall_dict):
    """
    Calculate the average monthly precipitation.

    Args:
        rainfall_dict (dict): Dictionary with month numbers as keys and rainfall in inches as values

    Returns:
        float: Average rainfall in inches
    """
    if not rainfall_dict:
        return 0.0

    total_rainfall = 0.0
    count = 0

    # Sum all rainfall values
    for rainfall in rainfall_dict.values():
        total_rainfall += rainfall
        count += 1

    # Calculate and return average
    return total_rainfall / count

def count_months_above_average(rainfall_dict):
    """
    Count how many months have precipitation above the average.

    Args:
        rainfall_dict (dict): Dictionary with month numbers as keys and rainfall in inches as values

    Returns:
        int: Number of months above average precipitation
    """
    if not rainfall_dict:
        return 0

    # Calculate average rainfall
    average = calculate_average_precipitation(rainfall_dict)
    count = 0

    # Count months above average
    for rainfall in rainfall_dict.values():
        if rainfall > average:
            count += 1

    return count

def bubble_sort_months_descending(rainfall_dict):
    """
    Sort months in descending order of precipitation using bubble sort.

    Args:
        rainfall_dict (dict): Dictionary with month numbers as keys and rainfall in inches as values

    Returns:
        list: List of tuples (month, rainfall) sorted in descending order
    """
    if not rainfall_dict:
        return []

    # Convert dictionary to list of tuples
    months_list = []
    for month, rainfall in rainfall_dict.items():
        months_list.append((month, rainfall))

    n = len(months_list)

    # Bubble sort algorithm
    for i in range(n):
        # Flag to check if any swaps were made
        swapped = False

        for j in range(0, n - i - 1):
            # Compare adjacent elements for descending order
            if months_list[j][1] < months_list[j + 1][1]:
                # Swap the elements
                temp = months_list[j]
                months_list[j] = months_list[j + 1]
                months_list[j + 1] = temp
                swapped = True

        # If no swaps, the list is sorted
        if not swapped:
            break

    return months_list

def inches_to_cm(inches):
    """
    Convert inches to centimeters.

    Args:
        inches (float): Measurement in inches

    Returns:
        float: Measurement in centimeters
    """
    return inches * 2.54

def get_month_name(month_number):
    """
    Convert month number to month name.

    Args:
        month_number (str): Month number as string (e.g., '01', '02')

    Returns:
        str: Full month name
    """
    month_names = {
        '01': 'January', '02': 'February', '03': 'March', '04': 'April',
        '05': 'May', '06': 'June', '07': 'July', '08': 'August',
        '09': 'September', '10': 'October', '11': 'November', '12': 'December'
    }

    return month_names.get(month_number, 'Unknown Month')