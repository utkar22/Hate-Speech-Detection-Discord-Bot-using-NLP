import csv

score = {}

def clean_score_dict():
    score = {}

def read_full():
    clean_score_dict()
    
    f = open("user_score.csv")

    csv_reader = csv.reader(f)

    for row in csv_reader:
        if (len(row) != 2):
            continue
        score[row[0]] = int(row[1])

def write_full():
    f = open("user_score.csv","w")

    csv_writer = csv.writer(f)

    for i in score:
        row = [i, score[i]]
        csv_writer.writerow(row)

def update_score(user_id, hate_score):
    read_full()
    user_id = str(user_id)

    print (user_id)
    print (score)
    print (user_id in score)

    if (user_id in score):
        score[user_id]+=hate_score
    else:
        score[user_id] = hate_score

    write_full()

def get_score(user_id):
    user_id = str(user_id)
    read_full()

    if (user_id in score):
        return score[user_id]
    return 0
