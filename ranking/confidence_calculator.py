def calculate_confidence(scores):

    weights = {

        "title": 30,
        "content": 35,
        "keyword": 15,
        "ui": 10,
        "page": 10

    }

    total = 0

    for key, weight in weights.items():

        total += scores.get(key, 0) * weight

    return round(total)