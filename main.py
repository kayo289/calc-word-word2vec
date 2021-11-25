from gensim.models import word2vec

sentences = word2vec.Text8Corpus("./twikiwp2-output.txt")
model = word2vec.Word2Vec(sentences, vector_size=200, min_count=20, window=15)
model.save("./wiki.model")
