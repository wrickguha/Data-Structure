import java.util.Scanner;

public class Stack {
    int size;
    int[] stack;

    Stack(int size){
        stack=new int[size];
    }

    void push(int top,int item)
    {
        if(top==size-1)
        {
            System.out.println("The Stack is full");
            return;
        }
        else
        {
            Scanner sc1= new Scanner(System.in);
            System.out.println("Enter the item: ");
            item=sc1.nextInt();
            top++;
            stack[top]=item;
            System.out.println("Item Inserted: "+item);
            sc1.close();
        }
    }
    void pop(int size,int top,int item)
    {
        if(top==-1)
        {
            System.out.println("The Stack is empty");
            return;
        }
        else
        {
            item=stack[top];
            top--;
            System.out.println("Item Deleted");
        }
    }
    void display()
    {
        if(top==-1)
        {
            System.out.println("The Stack is empty");
            return;
        }
        else
        {
            for(int i=0;i<size;i++)
            {
                System.out.println(stack[i]);
            }
        }
    }
    public static void main(String[] args) {
        Stack obj = new Stack();
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the size of the stack: ");
        int size = sc.nextInt();
        int top,item;
        Stack stack = new Stack(size);
        int ch;
        do{
            System.out.println("Enter the choice: ");
            ch=sc.nextInt();
            switch(ch)
            {
                case 1:
                obj.push();
                break;
                case 2:
                obj.pop();
                break;
                case 3:
                obj.display();
                break;
                case 4:
                System.exit (0);
                default:
                System.out.println("Invalid Input. Try Again!");
            }
        }while(ch!=4);
        sc.close();
    }
}
