# RenpyMusicWidget
_Простой виджет для вывода на экран играющей в данный момент музыки._

## Основная идея
В словарь **dict_d** записывается в формате _ключ:значение_ полный путь до файла музыки и название трека, которое необходимо вывести на экран.  В случае, если музыка не играет, [renpy.music.get_playing()](https://www.renpy.org/doc/html/audio.html?highlight=renpy%20music%20get_playing#renpy.music.get_playing) возвращает None, ключом указано, соответсвенно, None, а значением, например, "Сейчас ничего не играет." Далее используется **screen music_widget()**, в котором получается название играющего на данный момент файла, и, используя оператор [text](https://www.renpy.org/doc/html/screens.html#text), выводится название на экран. Опционально можно добавить созданный экран в [config.overlay_screens](https://www.renpy.org/doc/html/config.html?highlight=config%20overlay_screens#var-config.overlay_screens).

## Пример словаря
```python
music_d = {
    None: "Сейчас ничего не играет",
    "audio/PG_Silhouette": "Pastel Ghost — Silhouette",
    "audio/MegaDrive_Hexe": "Mega Drive — H.exe",
    "audio/MegaDrive_NARC": "Mega Drive — NARC"
}
```
