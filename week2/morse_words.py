# https://leetcode.com/problems/unique-morse-code-words/submissions/

class Solution:
    morse_alphabet = {"a":".-", "b":"-...", "c":"-.-.", "d":"-..", "e":".", "f":"..-.", "g":"--.", "h":"....", "i":"..",
                      "j":".---", "k":"-.-", "l":".-..", "m":"--", "n":"-.", "o":"---", "p":".--.", "q":"--.-", "r":".-.",
                      "s":"...", "t":"-", "u":"..-", "v":"...-", "w":".--", "x":"-..-", "y":"-.--", "z":"--.."}
    
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_words = set()
        for english_word in words:
            morse_word = ""
            for letter in english_word:
                morse_word += self.morse_alphabet[letter]
            morse_words.add(morse_word)
        
        return len(morse_words)