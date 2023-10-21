import java.util.Scanner;

public class Stack {
    int size;
    int stack[];
    int item,top;
    Stack(int size){
        this.size=size;
        this.stack= new int[size];
        this.top=-1;
       }
    void push()
    {
        if(top==size-1)
        {
            System.out.println("The stack is full");
            return;
        }
        else
        {
            Scanner sc1= new Scanner(System.in);
            System.out.println("Enter the item: ");
            item=sc1.nextInt();
            stack[top]=item;
            top++;
            System.out.println("Item Inserted");
            sc1.close();
        }
    }
    void pop()
    {
        if(top==-1)
        {
            System.out.println("The stack is empty");
            return;
        }
        else
        {
            top--;
            item=stack[top];
            System.out.println("Item deleted");
        }
    }
    void display()
    {
        if(top==-1)
        {
            System.out.println("the stack is empty");
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
        Scanner sc= new Scanner(System.in);
        System.out.println("Enter the size: ");
        int size= sc.nextInt();
        int ch;
        Stack stack = new Stack(size);
        do{
            System.out.println("1.\tPUSH\n2.\tPOP\n3.\tDISPLAY\n4.\tEXIT\n");
            System.out.println("Enter the choice: ");
            ch=sc.nextInt();
            switch(ch)
            {
                case 1:
                stack.push();
                break;
                case 2:
                stack.pop();
                break;
                case 3:
                stack.display();
                break;
                case 4:
                System.exit(0);
                default:
                System.out.println("Invalid input! Try again");
                break;
            }
        }while(ch!=4);
        sc.close();
    }
}
