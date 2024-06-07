class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dict_set = set(dictionary)
        sentence_li = sentence.split()

        seen_words = {}
        for i, word in enumerate(sentence_li):
            if word in seen_words:
                sentence_li[i] = seen_words[word]
                continue

            for j in range(len(word)):
                sub_word = word[:j+1]
                if sub_word in dict_set:
                    sentence_li[i] = sub_word
                    seen_words[word] = sub_word
                    break
        
        return " ".join(sentence_li)