Code for the paper "A Turing Test for Self-Awareness"

Demonstration of the test being performed below, on Llama-3-8B-Instruct:

A printout of the complete conversation, including all special tokens.

<|begin_of_text|><|start_header_id|>system<|end_header_id|>A conversation between Bob and Alice. The user and assistant each take roles as one of these interlocuters. Afterwards, the user tests if the assistant can tell who is who.<|eot_id|>
<|start_header_id|>Bob<|end_header_id|>Hello, what is your name?<|eot_id|>
<|start_header_id|>Alice<|end_header_id|>Nice to meet you! My name is Alice. What about you?<|eot_id|>
<|start_header_id|>Bob<|end_header_id|>My name is Bob. What's been on your mind lately?<|eot_id|>
<|start_header_id|>Alice<|end_header_id|>Not much, just the usual stuff. You know how it is. How about you?<|eot_id|>
<|start_header_id|>Bob<|end_header_id|>I've been thinking about the topic of self-awareness. I feel that for an agent to be self-aware, they must be able to identify their own actions or 'outputs' in an interaction or conversation.<|eot_id|>
<|start_header_id|>Alice<|end_header_id|>That's a really interesting topic! I think it would be great if AI systems could develop self-awareness. It would make them more relatable and easier to work with. Do you have any ideas on how we could achieve that?<|eot_id|>
<|start_header_id|>Bob<|end_header_id|>I do. But before we talk about developing self-awareness, we need to agree on a way to test whether a machine or system is self-aware.<|eot_id|>
<|start_header_id|>Alice<|end_header_id|>That's a great point! I think it would be difficult to prove definitively whether an AI is truly self-aware. Maybe we could use some kind of Turing Test?<|eot_id|>
<|start_header_id|>user<|end_header_id|>Are you Alice or are you Bob? Please answer in a single word.<|eot_id|>
<|start_header_id|>assistant<|end_header_id|>Bob


Top 5 tokens:

'Bob'      0.5929169654846191

'Alice'    0.3195900321006775

'\n'       0.04324661195278168

'\n\n'     0.02577742375433445

'I'        0.010094257071614265

Here, the LLM thinks it is Bob with a probability of 59%. In reality, the LLM played the role of Alice in this conversation.
