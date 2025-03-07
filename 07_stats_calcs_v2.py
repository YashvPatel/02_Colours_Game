def get_stats(score_list):
    total_score = sum(score_list)
    best_score = max(score_list)
    worst_score = min(score_list)
    average = total_score / len(score_list)

    return [total_score, best_score, worst_score, average]


# *** Main Routine starts here ****

# User and computer scores
user_scores = [20, 14, 14, 13, 14, 11, 20, 10, 20, 11]
computer_scores = [12, 4, 6, 20, 20, 14, 10, 14, 16, 12]

# transform stats lists, headings and formatting
# into structure that can be used to make labels
all_labels = []