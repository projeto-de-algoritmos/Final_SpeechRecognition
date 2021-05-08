from fastdtw import fastdtw
from python_speech_features import mfcc
from numpy import hamming

words = {}

def register_new_word(word: str, audio, samplerate: int):
    '''
    Inserts a new word into dataset
    Returns False if word already exists or if couldn't insert that word
    Return True in success
    '''
    success = True
    try:
        if word not in words:
            words[word] = mfcc(audio, samplerate, winfunc=hamming)
        else:
            success = False
    except:
        success = False
    
    return success

def query_word(audio, samplerate: int):
    '''
    Returns a sorted list of tuple(int, str) containing the distance between "audio"
    and every word present in dataset.
    First element from the tuple is the distance and the second one is the word compared.
    '''
    unknown_word = mfcc(audio, samplerate, winfunc=hamming)

    comparison_list = []
    for word in words:
        current_comparison, _ = fastdtw(unknown_word, word)
        comparison_list.append((current_comparison, word))

    return sorted(comparison_list)
