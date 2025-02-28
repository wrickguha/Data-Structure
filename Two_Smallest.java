import java.util.Arrays;

public class Two_Smallest {

    public static void findTwoSmallest(int[] arr) {
        int first_min=Integer.MAX_VALUE;
        int second_min = Integer.MAX_VALUE;
        int sum=0;
        
        for(int i=0;i<arr.length;i++)
        {
            if(arr[i]<first_min)
            {
                second_min=first_min;
                first_min=arr[i];
            }
            else if(arr[i]<second_min && arr[i]!=first_min)
            {
                second_min=arr[i];
            }
            sum=first_min+second_min;
        }
    }

    public static void main(String[] args) {
        int[] arr = {5, 8, 2, 1, 10, 6};
        findTwoSmallest(arr);
    }
}

