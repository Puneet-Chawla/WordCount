from collections import Counter
# frequency counter

text = "as as sd ew sd qw er qw sd svb v d df df sdfsd sdf  as qw er rt ty yu df ty yu gh yu cv cv vc vc"

word = text.split()
counter = Counter(word)
top_three = counter.most_common(3)
print(top_three)