words = ["sofa", "suitcase", "valise", "picture", "basket", "carton", "doggie"]
x = list(map(lambda w: sorted(w)[0], words))[5]
print(x)
