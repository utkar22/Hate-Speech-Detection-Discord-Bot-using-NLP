import pickle
import math

def get_models():
    model_hate = pickle.load(open("model_hate.sav","rb"))
    model_offensive = pickle.load(open("model_offensive.sav","rb"))

    return model_hate, model_offensive

model_hate, model_offensive = get_models()

def string_to_array(s):
    first_arr = s.split("and")

    final_arr = []

    for i in first_arr:
        i2 = i.lstrip().rstrip()
        str_builder = ""
        for j in i2:
            if (j not in (',','.','!','?','|','/')):
                str_builder+=j
            else:
                if (len(str_builder) > 0):
                    str_builder = str_builder.lstrip().rstrip()
                    final_arr.append(str_builder)
                    str_builder = ""

    str_builder = str_builder.lstrip().rstrip()
    final_arr.append(str_builder)

    final_arr_2 = []

    for i in final_arr:
        if (i):
            final_arr_2.append(i)
                    

    return final_arr_2

def get_slurs():
    f = open("slurs.txt")
    s = f.read()
    list_of_slurs = s.split("\n")
    return list_of_slurs

list_of_slurs = get_slurs()

def get_slur_score(arr):
    score_arr = []

    for i in arr:
        score = 0
        for j in list_of_slurs:
            if j in i:
                score+=1
        if score>3:
            score = 3
        score_arr.append(score)

    return score_arr

def get_hate_score(arr):
    hate_arr = model_hate.predict(arr)
    return hate_arr

def get_offensive_score(arr):
    offensive_arr = model_offensive.predict(arr)
    return offensive_arr

def calculate_final_score(slur_arr, hate_arr, offensive_arr):
    final_arr = []

    for i in range(len(slur_arr)):
        score = slur_arr[i] + hate_arr[i] + offensive_arr[i]
        final_arr.append(score)

    max_score = max(final_arr)
    avg_score = math.ceil(sum(final_arr)/len(final_arr))

    final_score = math.ceil(((max_score + avg_score)/3 + sum(slur_arr)/9)) // 3

    return final_score

def get_score(s):
    string_arr = string_to_array(s)

    if len(string_arr) == 0:
        return 0

    slur_score = get_slur_score(string_arr)
    hate_score = get_hate_score(string_arr)
    offensive_score = get_offensive_score(string_arr)

    #print (slur_score, hate_score, offensive_score)

    final_score = calculate_final_score(slur_score, hate_score, offensive_score)

    return final_score
        
