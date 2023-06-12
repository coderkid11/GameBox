def update_scores(username, score):
    scores = {}
    with open('scores.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                name, current_score = line.split(',')
                scores[name] = int(current_score)

    if username in scores:
        scores[username] = max(scores[username], int(score))
    else:
        scores[username] = int(score)

    with open('scores.txt', 'w') as file:
        for name, current_score in scores.items():
            file.write(f'{name},{current_score}\n')

    print('Score updated successfully.')
