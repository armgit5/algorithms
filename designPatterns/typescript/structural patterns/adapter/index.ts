class Target {
    public request(): string {
        return 'Target: The default target\'s behavior.';
    }
}

class Adaptee {
    public specificRequest(): string {
        return '.eetpadA eht fo roivaheb laicepS';
    }
}

class Adapter extends Target {
    
    constructor(private adaptee: Adaptee) {
        super();
    }

    public request(): string {
        const result = this.adaptee.specificRequest().split('').reverse().join('');
        return `Adapter: (TRANSLATED) ${result}`;
    }
}

const target = new Target();
console.log(target.request());

const adaptee = new Adaptee();
console.log(adaptee.specificRequest());

const adapter = new Adapter(adaptee);
console.log(adapter.request());