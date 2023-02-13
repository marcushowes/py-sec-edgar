from collections import Counter
import numpy as np
import math
import os
import Levenshtein
import nltk
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer


def cosine_similarity(string1, string2):
    words1 = string1.split()
    words2 = string2.split()
    counter1 = Counter(words1)
    counter2 = Counter(words2)
    terms = set(counter1).union(counter2)
    dotprod = sum(counter1.get(k, 0) * counter2.get(k, 0) for k in terms)
    mag1 = math.sqrt(sum(counter1.get(k, 0)**2 for k in counter1))
    mag2 = math.sqrt(sum(counter2.get(k, 0)**2 for k in counter2))
    return dotprod / (mag1 * mag2)


def jaccard_similarity(text1, text2):
    words1 = set(word_tokenize(text1))
    words2 = set(word_tokenize(text2))
    common_words = words1 & words2
    unique_words = words1 | words2
    return len(common_words) / len(unique_words)

def levenshtein_distance(text1, text2):
    distance = Levenshtein.distance(text1, text2)
    max_len = max(len(text1), len(text2))
    similarity = 1 - (distance / max_len)
    return similarity

def find_longest(string1, string2):
    length1 = len(string1)
    length2 = len(string2)
    length_difference = abs(length1 - length2)
    if length1 >= length2:
        string1 = "1"
        return (string1, length_difference)
    else:
        string2 = "2"
        return (string2, length_difference)

folderpath = r'C:\sec_gov\Archives\edgar\data\200406'
file1 = r'risk_factors_0000200406-21-000008.txt'
file2 = r'risk_factors_0000200406-22-000022.txt'

filepath1 = os.path.join(folderpath, file1)
filepath2 = os.path.join(folderpath, file2)

with open(filepath1, "r", encoding='utf-8') as f:
    text1 = f.read()

with open(filepath2, "r", encoding='utf-8') as f:
    text2 = f.read()

# Values of 1 = identical. 0 = completely different
cosine = cosine_similarity(text1, text2)
jaccard = jaccard_similarity(text1, text2)
levenshtein = levenshtein_distance(text1, text2)

(string, diff) = find_longest(text1, text2)

print(f"Cosine similarity = {cosine} \n")
print(f"Jaccard similarity = {jaccard} \n")
print(f"Levenshtein distance = {levenshtein} \n")
print(f"Text {string} is longer by {diff} characters.")


