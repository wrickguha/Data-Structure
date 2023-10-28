import java.util.Scanner;

public class i {
    int size;
    int stack[];
    int top = -1;

    // Constructor to initialize the stack array
    i(int size) {
        this.size = size;
        stack = new int[size];
    }

    void push() {
        if (top == size - 1) {
            System.out.println("The stack is full");
            return;
        } else {
            System.out.println("Enter the item: ");
            Scanner sc1 = new Scanner(System.in);
            int item = sc1.nextInt();
            top++;
            stack[top] = item;
            System.out.println("Item Inserted");
            sc1.close();
        }
    }

    void pop() {
        if (top == -1) {
            System.out.println("The stack is empty");
            return;
        } else {
            int item = stack[top];
            top--;
            System.out.println("Item deleted: " + item);
        }
    }

    void display() {
        if (top == -1) {
            System.out.println("The stack is empty");
            return;
        } else {
            for (int i = 0; i <= top; i++) {
                System.out.println(stack[i]);
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the size of the stack");
        int size = sc.nextInt();
        i stack = new i(size); // Create an instance of the Stack class with the specified size
        int ch;

        do {
            System.out.println("1. PUSH\n2. POP\n3. DISPLAY\n4. EXIT");
            System.out.println("Enter the choice: ");
            ch = sc.nextInt(); // Read the user's choice here

            switch (ch) {
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
                    break; // Make sure to break the loop after exiting
                default:
                    System.out.println("Invalid choice. Please enter a valid option.");
            }
        } while (ch != 4);
        sc.close();
    }
}
