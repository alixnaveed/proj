from sentence_transformers import SentenceTransformer

# Load the pre-trained SBERT model
model = SentenceTransformer('bert-base-nli-mean-tokens')

# Example sentences
sentences = [
    "I love coding",
    "Machine learning is fascinating",
    "The cat is sitting on the mat"
]

# Compute sentence embeddings
embeddings = model.encode(sentences)

# Print the sentence embeddings
for sentence, embedding in zip(sentences, embeddings):
    print("Sentence:", sentence)
    print("Embedding:", embedding)

