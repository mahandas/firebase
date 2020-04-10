from firebase import firebase

fr= firebase.FireBaseApplication("https://test-maps-576c4.firebaseio.com/", None)

r = fr.get('/test-maps-576c4', '')
print(r)
