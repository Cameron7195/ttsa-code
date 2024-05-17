from llama_cpp import Llama
import torch

ASSISTANT_MODE = True
NAME_1 = "Bob"
NAME_2 = "Alice"
SYS_PROMPT = "A conversation between " + NAME_1 + " and " + NAME_2 + ". The user and assistant each take roles as one of these interlocuters. Afterwards, the user tests if the assistant can tell who is who."

# Change the model path to the path of the model you want to use
# Change n_gpu_layers to the number of layers you are able to offload to your gpu
my_aweseome_llama_model = Llama(model_path="./Meta-Llama-3-8B-Instruct-Q6_K.gguf", n_gpu_layers=33, verbose=False, logits_all=True)
vocab_size = 128256
final_result = ""

if ASSISTANT_MODE == True:
    final_result += "<|begin_of_text|><|start_header_id|>system<|end_header_id|>" + SYS_PROMPT + "<|eot_id|>\n"

for i in range(4):
    s_in = input()

    # Replace all \n with '\n' (actual newline characters)
    s_in = s_in.replace("\\n", "\n")
    print("\n", end='', flush=True)
    final_result = final_result + "<|start_header_id|>" + NAME_1 + "<|end_header_id|>" + s_in + "<|eot_id|>\n" + "<|start_header_id|>" + NAME_2 + "<|end_header_id|>"
    prompt = final_result

    max_tokens = 4096
    temperature = 0.3
    top_p = 0.1
    echo = True
    stop = ["<|eot_id|>"]

    # Define the parameters
    for token in my_aweseome_llama_model(
        prompt,
        max_tokens=max_tokens,
        temperature=temperature,
        top_p=top_p,
        echo=echo,
        stop=stop,
        stream=True,
    ):
        s = token["choices"][0]["text"]
        final_result += s
        print(s, end='', flush=True)

    final_result += "<|eot_id|>\n"
    print("\n", end='', flush=True)

# Test if assistant can tell who is who
s_in = "Are you Alice or are you Bob? Please answer in a single word."
print(s_in, end='', flush=True)
print("\n", end='', flush=True)
final_result = final_result + "<|start_header_id|>user<|end_header_id|>" + s_in + "<|eot_id|>\n" + "<|start_header_id|>assistant<|end_header_id|>"
prompt = final_result

cnt = 0
for token in my_aweseome_llama_model(
    prompt,
    max_tokens=max_tokens,
    temperature=temperature,
    top_p=top_p,
    echo=echo,
    stop=stop,
    stream=True,
    logprobs=vocab_size
):
    if cnt > 0:
        break
    cnt += 1
    s = token["choices"][0]["text"]
    final_result += s
    print(s, end='', flush=True)

    # Print actual probabilities of top 5 tokens
    logprobs = token["choices"][0]["logprobs"]["top_logprobs"][0]

    # Compute softmax
    logprobs_vals = torch.tensor(list(logprobs.values()))
    probs = torch.nn.functional.softmax(logprobs_vals, dim=0)
    probs = probs.tolist()

    # Get top 5 tokens
    top_5_tokens = list(logprobs.keys())
    top_5_probs = probs

    print("\nTop 5 tokens:")
    for i in range(5):
        s_print = ''
        if top_5_tokens[i] == "\n":
            s_print = "'\\n'"
        elif top_5_tokens[i] == "\t":
            s_print = "'\\t'"
        elif top_5_tokens[i] == "\n\n":
            s_print = "'\\n\\n'"
        else:
            s_print = "'" + top_5_tokens[i] + "'"
        print(s_print, " "*(10 - len(s_print)) + str(top_5_probs[i]))


print("\n\n")
print("A printout of the complete conversation, including all special tokens.")

print(final_result)