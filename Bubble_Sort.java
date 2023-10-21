import java.util.Scanner;

public class Bubble_Sort {
    void Bubble(int arr[],int size){
        for(int i=0;i<size;i++)
        {
            for(int j=0;j<size-1;j++)
            {
                 if(arr[j]>arr[j+1])
                 {
                     int temp=arr[j];
                     arr[j]=arr[j+1];
                     arr[j+1]=temp;
                 }
            }
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the size: ");
        int size=sc.nextInt();
        int arr[]= new int[size];
        System.out.println("Enter the elements: ");
        for(int i=0;i<size;i++)
        {
            arr[i]=sc.nextInt();
        }
        Bubble_Sort obj= new Bubble_Sort();
        obj.Bubble(arr,size);
        System.out.println("After Sorting: ");
        for(int i=0;i<size;i++)
        {
            System.out.println(arr[i]);
        }
        sc.close();
    }
}
