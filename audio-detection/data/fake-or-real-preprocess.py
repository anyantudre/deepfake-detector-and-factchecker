import os
from datasets import Dataset, Audio, Value, ClassLabel, Features
from huggingface_hub import login

# Define the path to your dataset
dataset_path = "fake-or-real/for-norm"

# Initialize lists to store data
audio_paths = []
labels = []
sources = []

# Define label mapping
label_mapping = {"real": 0, "fake": 1}

# Traverse the dataset directory
for split in ["training", "validation", "testing"]:
    for label in ["real", "fake"]:
        folder_path = os.path.join(dataset_path, split, label)
        for file_name in os.listdir(folder_path):
            if file_name.endswith(".wav"):  # Assuming audio files are in .wav format
                file_path = os.path.join(folder_path, file_name)
                audio_paths.append(file_path)
                labels.append(label_mapping[label])
                sources.append("Fake-or-Real (FoR)")

# Create a Dataset
features = Features({
    "audio": Audio(sampling_rate=16000),
    "label": ClassLabel(names=["real", "fake"]),
    "source": Value("string")
})

dataset = Dataset.from_dict({
    "audio": audio_paths,
    "label": labels,
    "source": sources
}, features=features)

# Log in to Hugging Face Hub
login(token="")  # Replace with your actual token

# Push the dataset to the Hugging Face Hub
dataset.push_to_hub("anyantudre/fake_or_real_dataset")
