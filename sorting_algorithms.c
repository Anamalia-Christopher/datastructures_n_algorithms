#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>

void swap(int *, int *);
void bubble_sort_fn_call(int *, unsigned int);

int * selection_sort(int * arr, unsigned arrSize){
    int i;
    int j;
    int min;

    for(i=0; i<arrSize-1;i++){
        
        min=i;
        for ( j = i; j < arrSize; j++)
        {
            if (arr[min]> arr[j])
            min = j;

        }
        if(i==min)
        continue;
        swap(&arr[i], &arr[min]);
    
    }
    return arr;
}

void selection_sort_fn_call(int * arr, unsigned int size){
    int n = 0;
    printf("Selection sort on array: ");
    while(n!=5){
        printf("%d ", arr[n]);
        n++;
    }
    printf("\n");
    arr = selection_sort(arr, 5);
    printf("sorted array: ");
    n = 0;
    while(n!=5){
        printf("%d ", arr[n]);
        n++;
    }
    printf("\n");

}


int main() {
    unsigned int size = 5;
    int * arr = calloc(sizeof(int), size);
    // arr = {2, 10, 13, 123, 12};
    arr[4] = 2;
    arr[3] = 10;
    arr[2] = -13;
    arr[1] = 123;
    arr[0] = 12;
    
    
    selection_sort_fn_call(arr, size);
    bubble_sort_fn_call(arr, size);
    return 0;
}



int * bubble_sort(int * arr, unsigned int arrSize){
    int arrTraverse = 0;
    bool swapped = true;
    unsigned int i ;
    
    while (swapped==true || arrTraverse!=(arrSize-1) )

    {
        if (arrTraverse==(arrSize-1) && swapped==true){
            arrTraverse = 0;
            swapped = false;
        }

        if (arr[arrTraverse]> arr[arrTraverse+1]){
            swap(&arr[arrTraverse], &arr[arrTraverse+1]);
            swapped = true;

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


void bubble_sort_fn_call(int * arr, unsigned int size){
    int n = 0;
    printf("Bubble sort on array: ");
    while(n!=5){
        printf("%d ", arr[n]);
        n++;
    }
    printf("\n");
    arr = bubble_sort(arr, 5);
    printf("sorted array: ");
    n = 0;
    while(n!=5){
        printf("%d ", arr[n]);
        n++;
    }
    printf("\n");

}

