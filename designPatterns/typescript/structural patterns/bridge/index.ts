interface Implementation {
    operationImplementation(): string;
}

class Abstraction {
    protected implementation: Implementation;

    constructor(implementation: Implementation) {
        this.implementation = implementation;
    }

    public operation(): string {
        const result = this.implementation.operationImplementation();
        return `Abstraction: Base operation with:\n${result}`;
    }
}

class ConcreteImplementationA implements Implementation {
    public operationImplementation(): string {
        return 'ConcreteImplementationA: Here\'s the result on the platform A.';
    }
}

class ConcreteImplementationB implements Implementation {
    public operationImplementation(): string {
        return 'ConcreteImplementationB: Here\'s the result on the platform B.';
    }
}

let implementation = new ConcreteImplementationA();
let abstraction = new Abstraction(implementation);
console.log(abstraction.operation());

implementation = new ConcreteImplementationB();
abstraction = new Abstraction(implementation);
console.log(abstraction.operation());