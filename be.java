import java.util.Scanner;

public class StackUsingArray {

    private int maxSize;
    private int top;
    private int[] stackArray;

    public StackUsingArray(int maxSize) {
        this.maxSize = maxSize;
        this.stackArray = new int[maxSize];
        this.top = -1;
    }

    public void push(int value) {
        if (this.isStackFull()) {
            System.out.println("Stack Overflow. Cannot push to stack.");
        } else {
            this.top++;
            this.stackArray[this.top] = value;
        }
    }

    public int pop() {
        if (this.isStackEmpty()) {
            System.out.println("Stack Underflow. Cannot pop from stack.");
            return -1;
        } else {
            int poppedValue = this.stackArray[this.top];
            this.top--;
            return poppedValue;
        }
    }

    public int peek() {
        if (this.isStackEmpty()) {
            System.out.println("Stack Underflow. Cannot peek from stack.");
            return -1;
        } else {
            return this.stackArray[this.top];
        }
    }

    public boolean isStackEmpty() {
        return this.top == -1;
    }

    public boolean isStackFull() {
        return this.top == this.maxSize - 1;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the size of the stack:");
        int maxSize = scanner.nextInt();
        StackUsingArray stack = new StackUsingArray(maxSize);

        while (true) {
            System.out.println("1. Push");
            System.out.println("2. Pop");
            System.out.println("3. Peek");
            System.out.println("4. Exit");
            System.out.println("Enter your choice:");
            int choice = scanner.nextInt();
        }
    }