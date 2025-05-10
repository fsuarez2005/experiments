/*

https://en.wikipedia.org/wiki/Insertion_sort
Pseudo-code:
i ← 1
while i < length(A)
    j ← i
    while j > 0 and A[j-1] > A[j]
        swap A[j] and A[j-1]
        j ← j - 1
    end while
    i ← i + 1
end while

 */
package person.franksuarez.algorithms;

import java.util.List;

/**
 *
 * @author franksuarez
 */
public class InsertionSort {

    public static List<Integer> sort(List<Integer> data) {

//        i ← 1
        int i = 1;

//        while i < length(A)
        while (i < data.size()) {

//            j ← i
            int j = i;
//            while j > 0 and A[j-1] > A[j]
            while ((j > 0) && (data.get(j - 1) > data.get(j))) {

//                swap A[j] and A[j-1]
                int swap = data.get(j);
                data.set(j, data.get(j - 1));
                data.set(j - 1, swap);
//                j ← j - 1
                j -= 1;

//            end while
            }
//            i ← i + 1
            i += 1;
//        end while
        }
        return data;
    }

}
