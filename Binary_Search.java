import java.util.Scanner;

class Binary_Search{

void Binary(int[] arr,int target,int size)
{
    int beg=0,end=size-1,mid=(beg+end)/2;
    for(int i=0;i<size;i++)
    {
        if(arr[mid]==target)
        {
            System.out.println("The target is found");
            
        }
        else if(arr[mid]>target)
        {
            end=mid-1;
            mid=(beg+end)/2;
        }
        else
        {
            beg=mid+1;
            mid=(beg+end)/2;
        }
    }
    System.out.println("The element is not found");
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
        Binary_Search obj = new Binary_Search();
        obj.Binary(arr,size,target);
        sc.close();
    }
}