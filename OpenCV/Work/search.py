"""
pip install torch --index-url https://download.pytorch.org/whl/cpu
pip install sentence-transformers
pip install huggingface_hub[hf_xet]
"""

from sentence_transformers import SentenceTransformer, util
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# ===== Local KB =====
knowledge_base = {
    "i am feeling sick": "You should rest and drink plenty of water. If it persists, consult a doctor.",
    "my hand hurts": "Check if your hand is swollen or injured. Gentle movement may help, but see a doctor if pain continues.",
    "i have headache": "Try resting in a quiet room, stay hydrated, and avoid screens for a while.",
    "i want to learn python": "Start with basic syntax, loops, and functions. Then move on to projects to practice.",
    "i am stressed": "Take a short walk, breathe deeply, and try to relax. Stress management techniques help a lot."
}

# ===== Load Sentence Transformer for embeddings =====
model = SentenceTransformer('all-MiniLM-L6-v2')
kb_sentences = list(knowledge_base.keys())
kb_embeddings = model.encode(kb_sentences, convert_to_tensor=True)

# ===== Load GPT2 for local generation =====
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
gpt2_model = GPT2LMHeadModel.from_pretrained("gpt2")

def generate_local_response(prompt, max_length=50):
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = gpt2_model.generate(inputs, max_length=max_length, num_return_sequences=1)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

print("=== Intelligent Offline Assistant Started ===")
print("Type 'exit' or 'quit' to stop.\n")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() in ["quit", "exit"]:
        print("Assistant: Goodbye!")
        break

    # ----- Local KB Matching -----
    input_embedding = model.encode(user_input, convert_to_tensor=True)
    cosine_scores = util.pytorch_cos_sim(input_embedding, kb_embeddings)
    best_idx = torch.argmax(cosine_scores)
    best_score = cosine_scores[0][best_idx].item()

    if best_score >= 0.85:
        answer = knowledge_base[kb_sentences[best_idx]]
        print(f"Assistant (Local, Confidence {best_score:.2f}): {answer}")
    else:
        print("Assistant: Generating answer locally...")
        answer = generate_local_response(user_input)
        print(f"Assistant (Generated Locally): {answer}")
