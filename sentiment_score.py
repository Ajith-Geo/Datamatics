import json

def extract_score(json_string):
    data = json.loads(json_string)
    return data[0][0]["score"]

input_string = '''[[{"label": "LABEL_1", "score": 0.8286964893341064}, 
               {"label": "LABEL_0", "score": 0.08955524861812592}, 
               {"label": "LABEL_2", "score": 0.08174823224544525}]]'''

result = extract_score(input_string)
print(result)
