/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: asuwansiri
 *
 * Created on November 7, 2017, 4:25 PM
 * https://www.youtube.com/watch?v=CpjVucvAc3g&list=PL2_aWCzGMAwLZp6LMUKI3cc7pgGsasm2_&index=7
 */

#include <cstdlib>
#include <iostream>


using namespace std;

/*
 * 
 */

int Increment(int *a) {
    *a = *a + 1;
}

int SumOfElements(int A[], int size) {
    int i, sum = 0;
    for (i = 0; i < size; i++) {
        sum += A[i]; // is *(A+i)
    }
    return sum;
}
int main(int argc, char** argv) {

    int A[5] = {2,4,5,8,1};
    for (int i = 0; i < 5; i++) {
        cout << "Address = " << &A[i];
        cout << "Address = " << A+i;
        cout << "value = " << A[i];
        cout << "value = " << *(A+i);
        cout << "\n";
    }
    int size = sizeof(A)/sizeof(A[0]);
    int total = SumOfElements(A, size);
    cout << total;

    return 0;
}

