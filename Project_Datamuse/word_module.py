import requests

def synonym_words(word,num_results):

    url = f"https://api.datamuse.com/words?ml=on+top+of&max=" + str(num_results)
    r = requests.get(url)
    resu = r.json()
    words = [(res["word"],res["score"]) for res in resu]

    return(words)

print(synonym_words("on top of", 5))

def rhyme_words(word,num_results):
    
    url = f"https://api.datamuse.com/words?rel_rhy=grape&max=" + str(num_results)
    r = requests.get(url)
    resu = r.json()
    words = [(res["word"],res["score"]) for res in resu]
    
    return(words)
    
print(rhyme_words("grape", 5))

def antonym_words(word,num_results):
    url = f"https://api.datamuse.com/words?rel_ant=bright&max=" + str(num_results)
    r = requests.get(url)
    resu = r.json()
    words = [(res["word"]) for res in resu]
    
    return(words)
    
print(antonym_words("bright", 4))
    
    
if __name__ == "__main__":
    print(synonym_words("on top of", 5))
    print(rhyme_words("grape", 5))
    print(antonym_words("bright", 5))