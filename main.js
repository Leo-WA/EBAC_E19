// Classe Abstrata: Personagem
class Personagem {
    constructor(nome, nivel) {
        this.nome = nome;
        this.nivel = nivel;
    }

    displayInfo() {
        return `Nome: ${this.nome}, Nível: ${this.nivel}`;
    }
}

// Classe Herdeira: Guerreiro
class Guerreiro extends Personagem {
    constructor(nome, nivel, espada) {
        super(nome, nivel);  // Chamando o construtor da classe base
        this.espada = espada;  // Atributo específico de Guerreiro
    }

    displayInfo() {
        return `${super.displayInfo()}, Espada: ${this.espada}`;
    }
}

// Classe Herdeira: Mago
class Mago extends Personagem {
    constructor(nome, nivel, tipoMagia) {
        super(nome, nivel);  // Chamando o construtor da classe base
        this.tipoMagia = tipoMagia;  // Atributo específico de Mago
    }

    displayInfo() {
        return `${super.displayInfo()}, Tipo de Magia: ${this.tipoMagia}`;
    }
}

// Instâncias de objetos
const guerreiro1 = new Guerreiro("Arthur", 5, "Excalibur");  // Guerreiro com sua espada
const mago1 = new Mago("Merlin", 7, "Elemental");            // Mago com seu tipo de magia
const guerreiro2 = new Guerreiro("Lancelot", 4, "Claymore"); // Outro guerreiro com uma espada diferente

// Exibindo informações dos personagens
console.log(guerreiro1.displayInfo());
console.log(mago1.displayInfo());
console.log(guerreiro2.displayInfo());
