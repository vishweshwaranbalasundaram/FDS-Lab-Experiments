import pandas as pd
import json

# Structured Data
structured_data = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
})

print("Structured Data:\n", structured_data)

# Unstructured Data
unstructured_data = "This is an example of unstructured data. It can be a piece of text, an image, or a video file."

print("\nUnstructured Data:\n", unstructured_data)

# Semi-structured Data
semi_structured_data = {
    'ID': 1,
    'Name': 'Alice',
    'Attributes': {'Height': 165, 'Weight': 68}
}

print("\nSemi-structured Data:\n", semi_structured_data)

# Save output
with open("Experiment-01/outputs/1c_output.txt", "w") as f:
    f.write("Structured Data:\n")
    f.write(structured_data.to_string())
    f.write("\n\nUnstructured Data:\n")
    f.write(unstructured_data)
    f.write("\n\nSemi-structured Data:\n")
    f.write(json.dumps(semi_structured_data, indent=4))

print("\nOutput saved successfully!")
