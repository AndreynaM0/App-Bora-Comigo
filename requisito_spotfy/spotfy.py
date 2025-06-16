import usuarios.usuarios as moduloUsuario
import spotipy
from spotipy.oauth2 import SpotifyOAuth 

apiClientID = "3407794b77134edcb70b66ac5d7e5c54" 
apiSecret ="d0adf19898aa4581ab18a94c8efd7c02"

scope = 'playlist-modify-public' 
redirect_uri = "https://127.0.0.1:8888/callback"  

sp = None
user_id = None

def connectSpotfy () :    
    global sp
    global user_id
    
    if (sp == None):
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=apiClientID,
            client_secret=apiSecret,
            redirect_uri=redirect_uri,
            scope=scope,
            cache_path=".cache-Andreyna",
            requests_timeout=20
        ))

        user_info = sp.current_user()  
        user_id = user_info["id"]  


def criarPlaylist():
    playlist = sp.user_playlist_create(
        user=user_id,
        name= f"Playlist- Bora Comigo - {moduloUsuario.usuarioLogado["nome"]}", 
        public=True,             
        collaborative=True,      
        description= f"Playlist do usuário {moduloUsuario.usuarioLogado["nome"]}."
    ) 
    return playlist


def addMusicaNaPlaylist(artistasfile, carona):
    sp.trace = False
    tracks = []
    result = sp.search(artistasfile, limit=4) 
    for i, t in enumerate(result['tracks']['items']): 
        tracks.append(str(t['id'].strip( 'u' )))
        print("adicionando a música:", t['name'])
    while tracks:
        try:
            result = sp.user_playlist_add_tracks(user_id, carona["playlist"]["id"], tracks[:1]) 
        except:
            return False
        tracks = tracks[1:]
    return True


