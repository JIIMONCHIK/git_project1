import sqlite3
from pydub import AudioSegment


def build_music_file(self, name, wanted_name):
    con = sqlite3.connect(name)

    cur = con.cursor()

    result = cur.execute("""SELECT note, time FROM record""").fetchall()

    time = (result[0][1] * 1000) // 1
    sound_name = self.path + '/' + result[0][0] + self.format
    song = AudioSegment.from_file(sound_name, self.format[1:])[:time]   # весь файл
    pause = AudioSegment.from_file(sound_name, self.format[1:]) - 200
    # снижаем громкость на 200 децибел (это почти смертельно, так что файла с большей громкостью не будет)
    for i in range(1, len(result)):
        time = (result[i][1] * 1000) // 1
        if result[i][0] == 'Pause':
            song = song + pause[:time]
        else:
            sound_name = self.path + '/' + result[i][0] + self.format
            sound = AudioSegment.from_file(sound_name, self.format[1:])[:time]
            song = song + sound
    song.export(wanted_name, format='wav')