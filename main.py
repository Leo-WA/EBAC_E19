# Classe Abstrata: Personagem
class Personagem:
    def __init__(self, nome, nivel):
        # Inicializando atributos comuns a todos os personagens
        self.nome = nome
        self.nivel = nivel

    def display_info(self):
        # Método para exibir informações básicas do personagem
        return f"Nome: {self.nome}, Nível: {self.nivel}"

# Classe Herdeira: Guerreiro
class Guerreiro(Personagem):
    def __init__(self, nome, nivel, espada):
        super().__init__(nome, nivel)  # Chamando o construtor da classe base
        self.espada = espada  # Atributo específico de Guerreiro

    def display_info(self):
        # Método sobreescrito para incluir informações do guerreiro
        return f"{super().display_info()}, Espada: {self.espada}"

# Classe Herdeira: Mago
class Mago(Personagem):
    def __init__(self, nome, nivel, tipo_magia):
        super().__init__(nome, nivel)  # Chamando o construtor da classe base
        self.tipo_magia = tipo_magia  # Atributo específico de Mago

    def display_info(self):
        # Método sobreescrito para incluir informações do mago
        return f"{super().display_info()}, Tipo de Magia: {self.tipo_magia}"

# Instâncias de objetos
guerreiro1 = Guerreiro("Arthur", 5, "Excalibur")  # Guerreiro com sua espada
mago1 = Mago("Merlin", 7, "Elemental")          # Mago com seu tipo de magia
guerreiro2 = Guerreiro("Lancelot", 4, "Claymore")  # Outro guerreiro com uma espada diferente

# Exibindo informações dos personagens
print(guerreiro1.display_info())
print(mago1.display_info())
print(guerreiro2.display_info())
