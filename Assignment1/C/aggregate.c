#include "aggregate.h"
#include <stdio.h>
#include <stdlib.h>

// Returns min of elements in a given array
float min(float *arr, int size)
{
    if (arr == NULL || size <= 0)
    {
        printf("FATAL ERROR in line %d\n", __LINE__);
        exit(EXIT_FAILURE);
    }
    float min = arr[0];
    for (int i = 1; i < size; i++)
    {
        if (arr[i] < min)
        {
            min = arr[i];
        }
    }
    return min;
}

// Returns max of elements in a given array
float max(float *arr, int size)
{
    if (arr == NULL || size <= 0)
    {
        printf("FATAL ERROR in line %d\n", __LINE__);
        exit(EXIT_FAILURE);
    }
    float max = arr[0];
    for (int i = 1; i < size; i++)
    {
        if (arr[i] > max)
        {
            max = arr[i];
        }
    }
    return max;
}

// Returns sum of elements in a given array
float sum(float *arr, int size)
{
    if (arr == NULL || size <= 0)
    {
        printf("FATAL ERROR in line %d\n", __LINE__);
        exit(EXIT_FAILURE);
    }
    float sum = 0;
    for (int i = 0; i < size; i++)
    {
        sum += arr[i];
    }
    return sum;
}

// Returns average of elements in a given array
float avg(float *arr, int size)
{
    if (arr == NULL || size <= 0)
    {
        printf("FATAL ERROR in line %d\n", __LINE__);
        exit(EXIT_FAILURE);
    }
    return sum(arr, size) / size;
}

// Returns pseudo average of elements in a given array
float pseudo_avg(float *arr, int size)
{
    if (arr == NULL || size <= 0)
    {
        printf("FATAL ERROR in line %d\n", __LINE__);
        exit(EXIT_FAILURE);
    }
    return (min(arr, size) + max(arr, size)) / 2;
}
