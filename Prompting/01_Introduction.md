## 🔥🔥🔥**What is Prompt Engineering**
```
1. Prompt engineering is a modern discipline focused on developing and optimizing prompts for effective use of language models (LMs).  
2. It helps users understand the capabilities and limitations of large language models (LLMs).  
3. Researchers use prompt engineering to improve LLM performance on tasks such as question answering and arithmetic reasoning.  
4. Developers apply prompt engineering to design reliable prompting techniques that interact with LLMs and external tools.  
5. Prompt engineering goes beyond writing prompts and includes broader skills for working with and building systems using LLMs.  
6. It plays an important role in safely interacting with LLMs and improving their reliability.  
7. Prompt engineering can enhance models by adding domain knowledge and integrating external tools.  
8. Due to growing interest in LLM development, comprehensive prompt engineering guides have been created.  
9. These guides include research papers, advanced prompting methods, tutorials, model-specific strategies, lectures, references, and tools related to prompt engineering.

```
## 🔥🔥**Common LLM Prompt Settings**
```
🔹 When designing and testing prompts, users usually interact with a language model through an API.  
🔹 Different parameters can be adjusted to control how the model generates responses.  
🔹 Experimentation is often required to find the best settings for a specific use case.  
```

#### 🔥**Temperature**
```
🔹 Temperature controls randomness in model responses.  
🔹 A lower temperature produces more deterministic and factual outputs.  
🔹 A higher temperature increases randomness and creativity.  
🔹 Low temperature is suitable for factual tasks like question answering.  
🔹 High temperature works better for creative tasks such as poetry or storytelling.  
```

#### **🔥Top P (Nucleus Sampling)**
```
🔹 Top P controls how many probable tokens the model considers when generating text.  
🔹 A low Top P value results in more focused and predictable responses.  
🔹 A high Top P value allows more diverse and creative outputs.  
🔹 It is generally recommended to adjust either Temperature or Top P, but not both simultaneously.  
```
#### **🔥Max Length**
```
🔹 Max Length limits the number of tokens the model can generate.  
🔹 This helps prevent overly long responses and manage usage costs.  
```
#### **🔥Stop Sequences**
```
🔹 Stop sequences are predefined strings that tell the model when to stop generating text.  
🔹 They help control response structure and length, such as limiting list items.  
```

#### **🔥Frequency Penalty**
```
🔹 Frequency penalty reduces repetition by penalizing tokens that appear multiple times.  
🔹 Higher values decrease repeated words in the output.  
```

#### **🔥Presence Penalty**
```
🔹 Presence penalty discourages repeated tokens regardless of how often they appear.  
🔹 It promotes diversity and creativity in responses.  
🔹 Lower values help the model stay focused on a topic.  
🔹 Similar to Temperature and Top P, it is recommended to adjust either Frequency Penalty or Presence Penalty, not both together.  
🔹 Model behavior and results may vary depending on the specific LLM version being used.
```
---

### 🔥🔥🔥**Elements of a Prompt**
```
As we cover more and more examples and applications with prompt engineering, you will notice that certain elements make up a prompt.
A prompt contains any of the following elements: Persona, Task, Context and Output Format.
```

### **Persona (Role)**
```
🔹 Defines the role or character the model should assume.  
🔹 Influences the tone, expertise level, and style of the response.  
🔹 Example: Act as a teacher, software engineer, or marketing expert.  
```
### **Task**
```
🔹 Specifies the action the model must perform.  
🔹 Examples include explaining, summarizing, translating, generating code, or answering questions.  
```

### **Context**
```
🔹 Provides background information or additional details needed for better responses.  
🔹 Helps the model understand the situation, audience, or domain knowledge required.  
```

### **Output Format**
```
🔹 Defines how the response should be structured or presented.  
🔹 Examples include bullet points, step-by-step instructions, tables, or JSON format.  
🔹 A well-designed prompt combines persona, task, context, and output format to produce accurate and useful responses.
```
