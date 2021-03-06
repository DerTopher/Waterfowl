import arcade
import random

class Game(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, game_title):
        super().__init__(width, height, game_title)

        arcade.set_background_color(arcade.color.SKY_BLUE)


        # If you have sprite lists, you should create them here,
        # and set them to None
        self.player_list = None
        self.enten_list = None

    def setup(self):
        self.SCREEN_WIDTH = self.width
        self.SCREEN_HEIGHT = self.height
        self.SCREEN_BOTTOM = 0
        self.NAME_OF_THE_GAME = "Mallard Pursuit"
        self.background = None

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        # Create your sprites and sprite lists here
        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.enten_list = arcade.SpriteList(use_spatial_hash=True)


        # Score

        #Bulletcount
        self.bullets_in_magazine = 3
        self.bullets_shot = 0
        self.bullts_hit = 0
        self.bullets_missed = 0

        # Set up the player
        self.player_sprite = arcade.Sprite("images/sprites/Absehen.png", 0.25)
        self.player_list.append(self.player_sprite)


        # Set up the Duck
        #Todo: Der Sprite ist zu animieren.
        self.enten_sprite = arcade.Sprite("images/sprites/Ente1/e0.png", 0.3)
        self.enten_sprite.center_x = 64
        self.enten_sprite.center_y = 120
        self.enten_list.append(self.enten_sprite)

        #load sounds
        self.mossberg = arcade.load_sound("sounds/Mossberg500.ogg")
        self.walther = arcade.load_sound("sounds/Mein_Gott_Watlher.ogg")
        self.mossberg_happy = arcade.load_sound("sounds/Mossberg500-happy.ogg")
        self.Teckel = arcade.load_sound("sounds/Teckel.ogg")
        self.nachladen = arcade.load_sound("sounds/Mein_Gott_Watlher.ogg")

        self.music = arcade.load_sound("sounds/hintergrundgerausche.ogg")
        arcade.play_sound(self.music, 0.5, 0.0, True)

        #load background
        self.background = arcade.load_texture("images/scenery/layer0.png")
        self.layers = []
        for i in range (1, 4):
            self.layers.append(arcade.load_texture(f"images/scenery/layer{i}.png"))

        #load Ammo
        self.shotgunshells = arcade.load_texture("images/ammunition/shell.png")

    def on_draw(self):
        """
        Render the screen.
        """
        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()
        arcade.draw_texture_rectangle(
            self.SCREEN_WIDTH / 2,
            self.SCREEN_HEIGHT / 2,
            self.SCREEN_WIDTH,
            self.SCREEN_HEIGHT,
            self.background
        )

        ## TODO: Wieso erscheint die Ente trotzdem vor den Layern?
        self.enten_list.draw()

        for i in range(len(self.layers)):
            arcade.draw_texture_rectangle(
            self.SCREEN_WIDTH / 2,
            self.SCREEN_HEIGHT / 2,
            self.SCREEN_WIDTH,
            self.SCREEN_HEIGHT,
            self.layers[i])



        for i in range(self.bullets_in_magazine):
            arcade.draw_scaled_texture_rectangle(self.SCREEN_WIDTH - 30*i-20, 30, self.shotgunshells, 0.1)

        arcade.draw_text(
            self.NAME_OF_THE_GAME,
            self.SCREEN_WIDTH / 2,
            self.SCREEN_HEIGHT / 2 + self.SCREEN_HEIGHT / 3,
            (0, 0, 0,),
            anchor_x="center",
            font_size=100,
            font_name=("OpenBars", 'calibri', "arial")
        )




        arcade.draw_text(
            "Start Game",
            self.SCREEN_WIDTH / 2,
            self.SCREEN_HEIGHT / 2 + self.SCREEN_HEIGHT / 3 - 240,
            (0, 0, 0,),
            anchor_x="center",
            font_size=40,
            font_name=("OpenBars", 'calibri', "arial")
        )

        arcade.draw_text(
            "Credits",
            self.SCREEN_WIDTH / 2,
            self.SCREEN_HEIGHT / 2 + self.SCREEN_HEIGHT / 3 - 340,
            (0, 0, 0,),
            anchor_x="center",
            font_size=40,
            font_name=("OpenBars", 'calibri', "arial")
        )

        arcade.draw_text(
            "Exit",
            self.SCREEN_WIDTH / 2,
            self.SCREEN_HEIGHT / 2 + self.SCREEN_HEIGHT / 3 - 440,
            (0, 0, 0,),
            anchor_x="center",
            font_size=40,
            font_name=("OpenBars", 'calibri', "arial")
        )


        self.enten_list.draw()
        self.player_list.draw()


    #### TODO: Zufällig Enten generieren uns spawnen lassen
    #def entewuerfeln(self):
    #    zufall = random.randint(1, 6)
    #    if zufall == 6:
    #        self.enten_list.append(self.enten_sprite)


    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.enten_sprite.center_x = self.enten_sprite.center_x + 2
        self.enten_sprite.center_y = self.enten_sprite.center_y + 2

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        if key == arcade.key.H:
            arcade.play_sound(self.Teckel)

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x , y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        if button == arcade.MOUSE_BUTTON_LEFT:
            position_letzter_linksklick = [x, y]
            print("Letzter Linksklick: ", position_letzter_linksklick)
            if self.bullets_in_magazine:
                arcade.play_sound(self.mossberg_happy)
                self.bullets_in_magazine = self.bullets_in_magazine -1
            else:
                #TODO: Klicksound muss her
                #arcade.play_sound()
                print("leer")

        elif button == arcade.MOUSE_BUTTON_RIGHT:
            print("Nachladen")
            arcade.play_sound(self.nachladen)
            self.bullets_in_magazine = 3

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    """ Main method """
    game_title = "Mallard Pursuit"  # Denkbare Alternative: Hunt for Cocks
    game = Game(1920, 1000, game_title)
    game.setup()
    arcade.run()



if __name__ == "__main__":
    main()
