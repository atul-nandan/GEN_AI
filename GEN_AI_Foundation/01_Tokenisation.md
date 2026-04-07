## 🔥🔥**What is Tokenization?**
```
Tokenization is the process of converting human text into smaller units called tokens that an AI model can process.

Example:
    Sentence: "Generative AI is powerful"
    Possible tokens: ["Gener", "ative", " AI", " is", " powerful"]

    Each token is then mapped to a numeric ID.
```

### **🔥What is a Token?**
```
A token is not always a word.
It can be:
    ✅ Full word
    ✅ Part of a word
    ✅ Single character
    ✅ Space or punctuation

Example: 
    Simple words (1 token): "cat", "hello", "water".
    Complex/long words (2+ tokens):
    "waterfall" → 2 tokens ("water" + "fall")
    "darkness" → 2 tokens ("dark" + "ness")
    "hamburger" → 3 tokens ("ham" + "bur" + "ger")
    "unbelievable" → 3 tokens ("un" + "believ" + "able") 
```

⭐Rough rule:
```
1 token ≈ 3–4 characters (English)
1 word ≈ 1.33 tokens
1 token ≈ 0.75 words
100 tokens ≈ 75 words 
```

**🔥Language and Content Variation**

The token-to-word ratio varies significantly based on the language and the type of content being processed.
```
English	1 word ≈ 1.3 to 1.4 tokens
Code	1 word ≈ 2.0 tokens
French / German / Spanish	1 word ≈ 2.0 to 2.1 tokens
Chinese	1 word ≈ 2.5 tokens
Hindi	1 word ≈ 6.4 tokens
```

**🔥Types of Tokenization**

1️⃣ Word Tokenization
```
Splits by words.

"I love AI" → ["I", "love", "AI"]

❌ Problem: Huge vocabulary size.
```

2️⃣ Character Tokenization
```
Each character becomes a token.

AI → ["A", "I"]

✅ Flexible
❌ Too many tokens.
```

3️⃣ Subword Tokenization 
```
Used by modern LLMs (GPT 4o).

Common methods:
    Byte Pair Encoding (BPE)
    WordPiece
    SentencePiece

Example: unbelievable → un + believe + able
```
---
⭐ For More Please checkout: [ TikTokenizer by OpenAI ](https://tiktokenizer.vercel.app/?model=gpt-4o)

⭐ For More Please checkout: [ 01_tokenization.py ](../Code/01_tokenization.py)