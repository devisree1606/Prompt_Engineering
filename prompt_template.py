def build_prompt(technique, task):

    if technique == "Zero-shot":
        return f"""
Answer the following task directly and accurately.

Task:
{task}
""".strip()

    if technique == "One-shot":
        return f"""
Use the example below to understand the expected answer style.

Example:
Task: What is Python?
Answer: Python is a high-level programming language.

Now answer this task:
{task}
""".strip()

    if technique == "Two-shot":
        return f"""
Study the two examples and follow their style.

Example 1:
Task: What is AI?
Answer: AI is technology that enables machines to perform tasks
that normally require human intelligence.

Example 2:
Task: What is ML?
Answer: Machine learning is a part of AI that learns patterns
from data to make predictions.

Now answer this task:
{task}
""".strip()

    if technique == "Few-shot":
        return f"""
Study the examples and follow their style.

Example 1:
Task: What is AI?
Answer: AI enables machines to perform tasks requiring human intelligence.

Example 2:
Task: What is ML?
Answer: ML helps computers learn patterns from data.

Example 3:
Task: What is NLP?
Answer: NLP enables computers to understand and process human language.

Example 4:
Task: What is Python?
Answer: Python is a high-level programming language.

Now answer this task:
{task}
""".strip()

    if technique == "CoT":
        return f"""
Solve the task carefully.
Identify the important information, work through the solution
logically, and provide a concise final answer with a short
explanation of the key steps.
Do not reveal private internal reasoning.

Task:
{task}
""".strip()

    if technique == "Manual CoT":
        return f"""
Follow the explicit problem-solving structure below.

Step 1 - Understand the task:
Identify what is being asked.

Step 2 - Identify information:
List the important facts and constraints.

Step 3 - Apply the method:
Use the appropriate rule or method to solve the task.

Step 4 - Verify:
Check whether the answer is reasonable.

Step 5 - Final answer:
Provide the final answer clearly.

Task:
{task}
""".strip()

    if technique == "ToT":
        return f"""
Explore multiple possible approaches to solve the task.

Approach A:
Suggest one possible solution and briefly evaluate it.

Approach B:
Suggest another possible solution and briefly evaluate it.

Approach C:
Suggest a third possible solution when useful.

Selection:
Compare the approaches based on their suitability.

Final answer:
Choose a suitable approach and provide the answer
with a concise explanation.

Task:
{task}
""".strip()

    raise ValueError("Unknown prompting technique")