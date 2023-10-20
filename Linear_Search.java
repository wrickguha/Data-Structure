import java.util.Scanner;

public class Linear_Search {
    void Linear(int arr[],int size,int target)
    {
        for(int i=0;i<size;i++)
        {
            if(arr[i]==target)
            {
                System.out.println("The item is found");
                return;
            }
        }
        System.out.println("The item is not found");
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the size: ");
        int size= sc.nextInt();
        int arr[] = new int[size];
        System.out.println("Enter the elements: ");
        for(int i=0;i<size;i++)
        {
            arr[i]=sc.nextInt();
        }
        System.out.println("Enter the item to be searched: ");
        int target=sc.nextInt();
        Linear_Search obj= new Linear_Search();
        obj.Linear(arr, size, target);
        sc.close();
    }
}
