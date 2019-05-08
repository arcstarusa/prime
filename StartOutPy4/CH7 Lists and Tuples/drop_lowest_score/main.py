# This program gets a series of test scores and
# calculates the average of the scores with the
# lowest score dropped. 7-12
def main():
    # Get the test scores from the user.
    scores = get_scores()

    # Get the total of the test scores.
    total = get_total(scores)

    # Get the lowest test scores.
    lowest = min(scores)

    # Subtract the lowest score from the total.
    total -= lowest

    # Calculate the average. Note that we divide
    # by 1 less that the number of scores because
    # the lowest score was dropped.
    average = total / (len(scores) -1)

    # Display the average.
    print('The average, with the lowest score dropped', 'is:', average)