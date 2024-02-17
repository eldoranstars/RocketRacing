##### Game launch:
- git clone https://github.com/eldoranstars/RocketRacing.git
- cd RocketRacing
- pip install -r requirements.txt
- python game.py

##### Game structure:
- основной цикл игры game.py;
- все игровые ф-ции game_functions.py;
- все параметры игры settings.py;
- все настройки состояния stats.py;
- все классы в rects;
- Python 3.8.10

##### compile linux
pyinstaller -F --add-data "media/*:media" --add-data "rects/*:." --icon=favicon.ico game.py --name RocketRacing
##### compile windows
pyinstaller -F --add-data "media\*;media" --add-data "rects\*;." --icon=favicon.ico game.py --name RocketRacing