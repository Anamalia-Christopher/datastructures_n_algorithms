#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>

void swap(int *, int *);

int * bubble_sort(int * arr, unsigned int arrSize){
    int arrTraverse = 0;
    bool swapped = true;
    unsigned int i ;
    
    while (swapped==true && arrTraverse!=(arrSize-1) )

    {

        if (arr[arrTraverse]> arr[arrTraverse+1]){
            swap(&arr[arrTraverse], &arr[arrTraverse+1]);
            swapped = true;

        }
        if (arrTraverse==(arrSize-2) && swapped==true){
            arrTraverse = 0;
            swapped = false;
        }

        arrTraverse++;
    }
    
    return arr;
}

void swap(int * greater, int * lesser){


    *lesser = *lesser ^ *greater;
    *greater = *lesser ^ *greater;
    *lesser = *lesser ^ *greater;

}

int main() {

    int * arr = calloc(sizeof(int), 5);
    // arr = {2, 10, 13, 123, 12};
    arr[0] = 2;
    arr[1] = 10;
    arr[2] = 13;
    arr[3] = 123;
    arr[4] = 12;
    int n = 0;
    // while(n!=5){
    //     printf("%d ", arr[n]);
    //     n++;
    // }
    arr = bubble_sort(arr, 5);
    
    n = 0;
    while(n!=5){
        printf("%d ", arr[n]);
        n++;
    }
    return 0;
}