class Game:
    def __init__(self, background_active):
        # ustawiamy najważniejsze elementy, niektóre na stałe
        self.background_active = background_active
        self.background_position = (0, 0)

    def print_game(self):
        print(f"Wartość właściwości to {self.background_active}")

# definiujemy funkcję testową
def test_update():
    background_active = "nazwa_nowa_pliku"
    game.background_active = "jeszcze_inna_nazwa"

# tutaj test
background_active = "nazwa_pliku_01"
game = Game(background_active)
game.print_game()
game.background_active = "inna_nazwa"
game.print_game()

# teraz wywołamy funkcję testową
test_update()

# i sprawdzimy
game.print_game()
