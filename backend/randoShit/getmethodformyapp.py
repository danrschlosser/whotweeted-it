import ast


def getQuizData(filename):

    with open(filename, 'r') as f:
        s = f.read()
        dictionary = json.loads(s)

        



