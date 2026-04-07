
### 🔥🔥🔥**Few-Shot Prompting**
```
🔹 Although Large Language Models (LLMs) show strong zero-shot abilities, they may struggle with more complex tasks.  
🔹 "Few-shot prompting" improves performance by providing examples (demonstrations) inside the prompt.  
🔹 These demonstrations guide the model through "in-context learning", helping it understand how to perform the task correctly.  
🔹 The examples act as conditioning so the model can generate better responses for new inputs.  
```

### **Origin of Few-Shot Capabilities**
```
🔹 Research shows few-shot abilities emerged when models became sufficiently large.  
🔹 Scaling model size allowed LLMs to learn patterns directly from examples provided in prompts.  
```
### **Few-Shot Prompting Example**
```
🔹 Task: Use a newly defined word in a sentence.

Prompt: A "whatpu" is a small, furry animal native to Tanzania.
Example: We were traveling in Africa and we saw these very cute whatpus.

prompt: To do a "farduddle" means to jump up and down really fast.
Example: ?

Output => When we won the game, we all started to farduddle in celebration.

🔹 The model learns the task from just one example (**1-shot prompting**).  
🔹 Increasing examples (3-shot, 5-shot, 10-shot) can help with harder tasks.
```
  

### **Important Tips for Few-Shot Demonstrations**
```
🔹 The label space and input distribution used in examples strongly influence performance.  
🔹 Prompt format is important — structured demonstrations work better than no examples.  
🔹 Even randomly assigned labels can still help performance compared to zero-shot prompting.  
🔹 Using labels sampled from realistic distributions improves results further.  
```

### **Example with Random Labels**
```
Prompt:
This is awesome!        // Negative
This is bad!            // Positive
Wow that movie was rad! // Positive
What a horrible show!   //  ?

Output => Negative

🔹 The model predicts correctly despite randomized labels because the example structure guides learning.  
```

### **Flexible Formatting**
```
🔹 Newer LLMs can still perform well even when prompt formatting is inconsistent.  
🔹 This shows increased robustness of modern models.  
```

### **Limitations of Few-Shot Prompting**
```
🔹 Few-shot prompting works well for many tasks but struggles with complex reasoning problems.  
🔹 Example reasoning task:- The odd numbers in this group add up to an even number: 15, 32, 5, 13, 82, 7, 1
🔹 The model incorrectly concluded the sum was even, showing reasoning limitations.  
🔹 Adding several examples still failed to produce reliable reasoning results.  
```

### **Why Few-Shot Sometimes Fails**
```
🔹 Some tasks require multi-step reasoning rather than pattern matching.  
🔹 Simply showing examples may not teach the reasoning process itself.  
```
### **Next Step: Advanced Prompting**
```
🔹 When zero-shot and few-shot prompting are insufficient, consider:
        - Breaking problems into reasoning steps  
        - Using advanced prompting techniques  
        - Fine-tuning models  

🔹 "Chain-of-Thought (CoT) prompting" was introduced to improve performance on arithmetic, commonsense, and symbolic reasoning tasks.
```