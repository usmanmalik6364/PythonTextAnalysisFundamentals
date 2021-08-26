from transformers import pipeline
classifier = pipeline("zero-shot-classification")
# zero-shot-classification pipeline allows us to specify labels for classification.
result = classifier("I'm learning about hugging face library and it seems nice",
                    candidate_labels=["education", "politics", "business"])
# The nice feature about zero-shot-classification pipeline is that we can provide it with
# labels and then it returns us a result with confidence score if the specified text belongs to that label.

print(result)
