from models import db, connect_db, Playlist, Song, PlaylistSong
from app import app

db.drop_all()
db.create_all()

# Clear query
Playlist.query.delete()
Song.query.delete()
PlaylistSong.query.delete()

p1 = Playlist(name="Test", description="Testing 123...")
p2 = Playlist(name="Test 1", description="Testing 123456789...")
p3 = Playlist(name="Favorite Playlist", description="Favorite songs")
p4 = Playlist(name="Rock and Roll", description="Rock you")
p5 = Playlist(name="Hip Hop", description="Hippity Hop Hop")
p6 = Playlist(name="Techno", description="Strictly Techno")

playlists = [p1, p2, p3, p4, p5, p6]

db.session.add_all(playlists)
db.session.commit()

s1 = Song(title="My Song", artist="ME")
s2 = Song(title="My Other Song", artist="ME")
s3 = Song(title="Paper Planes", artist="MIA")
s4 = Song(title="Colors", artist="RED")
s5 = Song(title="Angry Birds", artist="Tweetz")
s6 = Song(title="Thunderstruck", artist="ACDC")
s7 = Song(title="Intergalactic", artist="Beastie Boys")
s8 = Song(title="Sandstorm", artist="Darud")
s9 = Song(title="Thizz Dance", artist="Mac Dre")
songs = [s1, s2, s3, s4, s5, s6, s7, s8, s9]

db.session.add_all(songs)
db.session.commit()

ps1 = PlaylistSong(playlist_id=1, song_id=1)
ps2 = PlaylistSong(playlist_id=1, song_id=2)
ps3 = PlaylistSong(playlist_id=2, song_id=2)
ps4 = PlaylistSong(playlist_id=3, song_id=3)
ps5 = PlaylistSong(playlist_id=1, song_id=4)
ps6 = PlaylistSong(playlist_id=2, song_id=5)
ps7 = PlaylistSong(playlist_id=1, song_id=5)
ps8 = PlaylistSong(playlist_id=3, song_id=6)
ps9 = PlaylistSong(playlist_id=4, song_id=6)
ps10 = PlaylistSong(playlist_id=5, song_id=7)
ps11 = PlaylistSong(playlist_id=5, song_id=9)
ps12 = PlaylistSong(playlist_id=6, song_id=8)

song_playlists = [ps1, ps2, ps3, ps4, ps5,
                  ps6, ps7, ps8, ps9, ps10, ps11, ps12]

db.session.add_all(song_playlists)
db.session.commit()
