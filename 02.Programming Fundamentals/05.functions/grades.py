def grades_in_text(score):
    if 2.00 <= score < 3.00:
        return 'Fail'
    if 3.00 <= score < 3.50:
        return 'Poor'
    if 3.50 <= score < 4.50:
        return 'Good'
    if 4.50 <= score < 5.50:
        return 'Very Good'
    if 5.50 <= score <= 6.00:
        return 'Excellent'  # we don't use elif because we use returns. you can also score = \
        # string and use print score with elifs


score_data = float(input())
print(grades_in_text(score_data))
