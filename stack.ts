
class Stack<T> {
    private array: T[] = []
    private top: number = -1;

    constructor() {

    }

    push(value: T) {
        this.array.push(value);
        this.top++;
    }

    pop(): T {
        if (this.top == -1) {
            throw new Error("Stack Underflow")
        }
        return this.array[this.top--]
    }

    print(): void {
        console.log(this.array)
    }

}

const myStack = new Stack<number>();

myStack.push(5);
myStack.push(7);
myStack.push(1);
console.log(myStack.pop());
myStack.print();