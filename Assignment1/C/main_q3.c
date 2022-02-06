
#include <stdio.h>
#include "aggregate.h"

int main(int argc, const char *argv[])
{
    float arr1[] = {27.1738, 88.32197, 93.97, 28.9, 7.043};
    float arr2[] = {37.455, 5.32, 37.056, 54.9891, 0.35, 15.0844, 19.79, 67.6981, 68.358, 27.8};

    // Array of function pointers containing pointers to functions in aggregate.c
    float (*aggregates[5])(float[], int) = {&min, &max, &sum, &avg, &pseudo_avg};

    for (int i = 0; i < 5; i++)
    {
        printf("\n%f\n%f\n", (*aggregates[i])(arr1, 5), (*aggregates[i])(arr2, 10));
    }

    printf("\n");

    return 0;
}