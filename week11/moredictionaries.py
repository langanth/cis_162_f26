
streaming = {}
streaming["Netflix"] = ["movies", "shows"]
streaming["Spotify"] = ["music", "podcasts"]
streaming["Hulu"] = ["movies", "shows"]

print(streaming)

streaming["Netflix"].append("video games")

for i in streaming:
    print(i)

for i in streaming.keys():
    print(i)

for i in streaming.values():
    print(i, len(i))

for i in streaming.items():
    print(i)

for k, v in streaming.items():
    print(k)
    print(v)