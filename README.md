# Something with ducks
A little journey to create something with ducks :duck: :duck:

### Warning
When trying to run the program from source code users of Arch Linux (possibly other Distros arr affected as well) might encounter problems when drawing text via python arcade.
<br><br><b>  Solution: </b> Manually uninstall Pillow via pip:
    `sudo pip uninstall Pillow`
  <br>Then recompile Pillow yourself:
  `pip install --compile --install-option=-O1 Pillow`


### Steps
1. Install virtual environment `python3 -m venv .env`
1. Activate with `. .env/bin/activate`, deactivate with `deactivate`
1. With activated .env, install required modules `pip install -r requirements.txt`
1. Follow [RealPython Tutorial](https://realpython.com/arcade-python-game-framework/#basic-arcade-program) from here

### Resources
- [https://arcade.academy/](https://arcade.academy/)

### Contributors
@cmacht
@dertopher