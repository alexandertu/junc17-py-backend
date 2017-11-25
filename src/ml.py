import numpy as np
import sklearn as sk

tr = {
"id":"1JI70l1lE5IF2tgJm5TnMD",
   "info":{  
      "album":{  
         "album_type":"single",
         "artists":[  
            {  
               "external_urls":{  
                  "spotify":"https://open.spotify.com/artist/69GGBxA162lTqCwzJG5jLp"
               },
               "href":"https://api.spotify.com/v1/artists/69GGBxA162lTqCwzJG5jLp",
               "id":"69GGBxA162lTqCwzJG5jLp",
               "name":"The Chainsmokers",
               "type":"artist",
               "uri":"spotify:artist:69GGBxA162lTqCwzJG5jLp"
            }
         ],
         "available_markets":[  
            "AD",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "EC",
            "EE",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IS",
            "IT",
            "JP",
            "LI",
            "LT",
            "LU",
            "LV",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NO",
            "NZ",
            "PA",
            "PE",
            "PH",
            "PL",
            "PT",
            "PY",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TR",
            "TW",
            "US",
            "UY",
            "VN"
         ],
         "external_urls":{  
            "spotify":"https://open.spotify.com/album/3oS6pMqcIiHaq3B47mDop5"
         },
         "href":"https://api.spotify.com/v1/albums/3oS6pMqcIiHaq3B47mDop5",
         "id":"3oS6pMqcIiHaq3B47mDop5",
         "images":[  
            {  
               "height":640,
               "url":"https://i.scdn.co/image/6f32f7a8c32f904e7ffe738ecbaf374456825348",
               "width":640
            },
            {  
               "height":300,
               "url":"https://i.scdn.co/image/67057ea332a06b2df8df155d51de252a12ca55d8",
               "width":300
            },
            {  
               "height":64,
               "url":"https://i.scdn.co/image/6da04358658336c7af750af196dc5305a0a0eb41",
               "width":64
            }
         ],
         "name":"Don't Let Me Down (Hardwell & Sephyx Remix)",
         "type":"album",
         "uri":"spotify:album:3oS6pMqcIiHaq3B47mDop5"
      },
      "artists":[  
         {  
            "external_urls":{  
               "spotify":"https://open.spotify.com/artist/69GGBxA162lTqCwzJG5jLp"
            },
            "href":"https://api.spotify.com/v1/artists/69GGBxA162lTqCwzJG5jLp",
            "id":"69GGBxA162lTqCwzJG5jLp",
            "name":"The Chainsmokers",
            "type":"artist",
            "uri":"spotify:artist:69GGBxA162lTqCwzJG5jLp"
         },
         {  
            "external_urls":{  
               "spotify":"https://open.spotify.com/artist/6Dd3NScHWwnW6obMFbl1BH"
            },
            "href":"https://api.spotify.com/v1/artists/6Dd3NScHWwnW6obMFbl1BH",
            "id":"6Dd3NScHWwnW6obMFbl1BH",
            "name":"Daya",
            "type":"artist",
            "uri":"spotify:artist:6Dd3NScHWwnW6obMFbl1BH"
         },
         {  
            "external_urls":{  
               "spotify":"https://open.spotify.com/artist/6BrvowZBreEkXzJQMpL174"
            },
            "href":"https://api.spotify.com/v1/artists/6BrvowZBreEkXzJQMpL174",
            "id":"6BrvowZBreEkXzJQMpL174",
            "name":"Hardwell",
            "type":"artist",
            "uri":"spotify:artist:6BrvowZBreEkXzJQMpL174"
         },
         {  
            "external_urls":{  
               "spotify":"https://open.spotify.com/artist/7MXzeG7zoG8pKpqKCOqcZL"
            },
            "href":"https://api.spotify.com/v1/artists/7MXzeG7zoG8pKpqKCOqcZL",
            "id":"7MXzeG7zoG8pKpqKCOqcZL",
            "name":"Sephyx",
            "type":"artist",
            "uri":"spotify:artist:7MXzeG7zoG8pKpqKCOqcZL"
         }
      ],
      "available_markets":[  
         "AD",
         "AR",
         "AT",
         "AU",
         "BE",
         "BG",
         "BO",
         "BR",
         "CA",
         "CH",
         "CL",
         "CO",
         "CR",
         "CY",
         "CZ",
         "DE",
         "DK",
         "DO",
         "EC",
         "EE",
         "ES",
         "FI",
         "FR",
         "GB",
         "GR",
         "GT",
         "HK",
         "HN",
         "HU",
         "ID",
         "IE",
         "IS",
         "IT",
         "JP",
         "LI",
         "LT",
         "LU",
         "LV",
         "MC",
         "MT",
         "MX",
         "MY",
         "NI",
         "NL",
         "NO",
         "NZ",
         "PA",
         "PE",
         "PH",
         "PL",
         "PT",
         "PY",
         "SE",
         "SG",
         "SK",
         "SV",
         "TH",
         "TR",
         "TW",
         "US",
         "UY",
         "VN"
      ],
      "disc_number": 1,
      "duration_ms": 162440,
      "explicit": False,
      "external_ids": {  
         "isrc": "USQX91601142"
      },
      "external_urls": {  
         "spotify": "https://open.spotify.com/track/1JI70l1lE5IF2tgJm5TnMD"
      },
      "href": "https://api.spotify.com/v1/tracks/1JI70l1lE5IF2tgJm5TnMD",
      "id": "1JI70l1lE5IF2tgJm5TnMD",
      "name": "Don't Let Me Down - Hardwell & Sephyx Remix",
      "popularity": 61,
      "preview_url": "https://p.scdn.co/mp3-preview/ceefd8d635958ed2c06d2ea0bfc6dd05950097c1?cid=dc08370fa5224053aedca4f92e85e55a",
      "track_number": 1,
      "type": "track",
      "uri": "spotify:track:1JI70l1lE5IF2tgJm5TnMD"
   },
   "features":  
      {  
         "danceability":0.509,
         "energy":0.897,
         "key":8,
         "loudness":-3.418,
         "mode":0,
         "speechiness":0.0454,
         "acousticness":0.0861,
         "instrumentalness":0.000634,
         "liveness":0.0625,
         "valence":0.283,
         "tempo":149.864,
         "type":"audio_features",
         "id":"1JI70l1lE5IF2tgJm5TnMD",
         "uri":"spotify:track:1JI70l1lE5IF2tgJm5TnMD",
         "track_href":"https://api.spotify.com/v1/tracks/1JI70l1lE5IF2tgJm5TnMD",
         "analysis_url":"https://api.spotify.com/v1/audio-analysis/1JI70l1lE5IF2tgJm5TnMD",
         "duration_ms":162440,
         "time_signature":4
      }
}

tracks = list()
tracks.append(tr)

array = []

def convert_to_array(track):
    energy = track["features"]["energy"]
    tempo = track["features"]["tempo"]
    danceability = track["features"]["danceability"]
    loudness = track["features"]["loudness"]

    return [energy, tempo, danceability, loudness]

for track in tracks:
    array.append(convert_to_array(track))

final_array = np.array(array)    

print(final_array)