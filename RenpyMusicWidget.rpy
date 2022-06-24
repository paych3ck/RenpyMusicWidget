screen music_widget():
    $ current_music = renpy.music.get_playing("music")

    text music_d[current_music]

init python:
    music_d = {
        None: "Сейчас ничего не играет.",
        "audio/track_number_one.mp3": "TrackNumberOne.",
    }

    config.overlay_screens.append("music_widget")