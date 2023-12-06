class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        if self.tipo == 'mago':
            ataque = 'usou magia'
        elif self.tipo == 'guerreiro':
            ataque = 'usou espada'
        elif self.tipo == 'monge':
            ataque = 'usou artes marciais'
        elif self.tipo == 'ninja':
            ataque = 'usou shuriken'
        else:
            ataque = 'usou um ataque indefinido'

        print(f"O {self.tipo} atacou usando {ataque}")


heroi1 = Heroi('Gandalf', 150, 'mago')
heroi1.atacar()  # Saída: O mago atacou usando usou magia

heroi2 = Heroi('Lancelot', 35, 'guerreiro')
heroi2.atacar()  # Saída: O guerreiro atacou usando usou espada

heroi3 = Heroi('Bruce Lee', 32, 'monge')
heroi3.atacar()  # Saída: O monge atacou usando usou artes marciais

heroi4 = Heroi('Hanzo', 28, 'ninja')
heroi4.atacar()  # Saída: O ninja atacou usando usou shuriken
