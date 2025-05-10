/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package person.franksuarez.algorithms;

import java.util.List;

/**
 *
 * @author franksuarez
 */
public class BubbleSort {
    
    
    public static void sort(List<Integer> data) {
//        procedure bubbleSort(A : list of sortable items)
//    n := length(A)

    int n = data.size();
    
    boolean swapped = true;
            

//    repeat
    while (swapped) {

//        swapped := false
        swapped = false;


//        for i := 1 to n-1 inclusive do
        for (int i = 1; i <= n - 1; i++) {


//            { if this pair is out of order }

            

//            if A[i-1] > A[i] then
            if (data.get(i-1) > data.get(i)) {
//                { swap them and remember something changed }
//                swap(A[i-1], A[i])
                int swapvar = data.get(i-1);
                data.set(i-1, data.get(i));
                data.set(i, swapvar);
//                swapped := true
                swapped = true;
//            end if
            } // if (data.get(i-1) > data.get(i)) {
//        end for
        } // for (int i = 1; i <= n - 1; i++)
//    until not swapped
    } // while (swapped)
//end procedure
        
        
    }
}
