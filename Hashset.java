import java.util.HashSet;
import java.util.Iterator;
public class Hashset {
    public static void main(String[] args) {
        HashSet<Integer> set = new HashSet<>();

        //Insertion
        set.add(1);
        set.add(2);
        set.add(2);
        set.add(4);

        //size
        System.out.println("Size of the set is: "+set);

        //print all elements
        System.out.println(set);


        //search-contains
        if(set.contains(1))
        {
            System.out.println("Set contains 1");
        }
        if(!(set.contains(6)))
        {
            System.out.println("Set does not contain 6");
        }

        //deletion
        set.remove(1);
        if(!set.contains(1))
        {
            System.out.println("Does not contain 1");
        }

        //Iterator
        Iterator it = set.iterator();

        //hasnext, next

        while(it.hasNext())
        {
            System.out.println(it.next());
        }


    }
}
