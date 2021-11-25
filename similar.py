from gensim.models import word2vec
import sys

positive_list = []
negative_list = []

#if len(sys.argv) == 2:
#    p_list = sys.argv[1].strip("+").split("+")
#    n_list = sys.argv[2].strip("-").split("-")

model = word2vec.Word2Vec.load("./wiki.model")
results = model.wv.most_similar(positive=["人間"], negative=["睡眠"])

print("==式==")
print("人間-睡眠")
print("===上位3個の回答==")
for result in results[:3]:
    print(result[0])
