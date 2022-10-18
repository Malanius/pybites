import itertools as it

scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
belts = "white yellow orange green blue brown black paneled red".split()


def get_belt(user_score, scores=scores, belts=belts):
    print(f"User score: {user_score}")
    if user_score < scores[0]:
        return None
    acquired_belts = it.takewhile(lambda x: x[0] <= user_score, zip(scores, belts))
    return list(acquired_belts)[-1][1]