import json
import os
import matplotlib.pyplot as plt
import pandas as pd

def generate_math401():
    filepath = "original-data/math401.json"
    outputpath = "original-data-transformed/math401_transformed.json"
    
    """STRUCTURE:
    {"query": "4+3=", "response": "7"}
    """
    output_data = []
    
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            data = json.loads(line)
            try:
                answer = float(data["response"])  
            except ValueError:
                print("Error: Invalid response value: ", data["response"])
                
            transformed_data = {
                        "category": "Arithmetic",
                        "subcategory": None,
                        "question": data["query"],
                        "answer": answer,
                        "reasoning": None,
                        "source": "Math-401"
                        }
            
            output_data.append(transformed_data)

    with open(outputpath, 'w', encoding='utf-8') as outfile:
        json.dump(output_data, outfile, indent=4, ensure_ascii=False) 
        
def generate_mathematics_dataset():
    all_data = []

    for filename in os.listdir("original-data/mathematics_dataset-v1.0/train-easy"):
        if filename.endswith(".txt"):  # Check if the file is a text file
            subcategory = filename.split('__')[1].split('.')[0]  # Extract subcategory from the filename

            with open(os.path.join("original-data/mathematics_dataset-v1.0/train-easy", filename), 'r', encoding='utf-8') as file:
                lines = file.readlines()  # Read all lines into a list
                # Process each question-answer pair
                for i in range(0, len(lines), 2):
                    question = lines[i].strip() if i < len(lines) else None
                    answer = lines[i+1].strip() if i+1 < len(lines) else None

                    data = {
                        "category": "Arithmetic",
                        "subcategory": subcategory,
                        "question": question,
                        "answer": answer,
                        "reasoning": None,
                        "source": "Mathematics Dataset (Google DeepMind)"  # Adjust source as needed
                    }
                    all_data.append(data)

    # Write all data to a single JSON file
    with open("original-data-transformed/mathematics-dataset_transformed.json", 'w', encoding='utf-8') as outfile:
        json.dump(all_data, outfile, indent=4, ensure_ascii=False)
        
def filter_out_non_numeric_answers(input_file, output_file):
    """ Filters out answers that cannot be converted to floats and converts all others to float. """
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    filtered_data = []
    filtered_out = 0
    for d in data:
        answer = d['answer']
        if isinstance(answer, (int, float)):  # Already a number, convert to float
            d['answer'] = float(answer)
            filtered_data.append(d)
        elif isinstance(answer, str) and is_convertible_to_float(answer):  # Check if the string can be converted
            d['answer'] = float(answer)
            filtered_data.append(d)
        else:
            filtered_out += 1

    print("Filtered out", filtered_out, "non-numeric answers.")
    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(filtered_data, outfile, indent=4, ensure_ascii=False)
        
def is_convertible_to_float(value):
    """ Helper function to check if a string can be safely converted to float. """
    try:
        float(value)
        return True
    except ValueError:
        return False
        
def merge_json_files(file1, file2, output_file):
    with open(file1, 'r', encoding='utf-8') as f1:
        data1 = json.load(f1)
    with open(file2, 'r', encoding='utf-8') as f2:
        data2 = json.load(f2)
    combined_data = data1 + data2
    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(combined_data, outfile, indent=4, ensure_ascii=False)


def json_to_csv(json_file_path, csv_file_path):
    df = pd.read_json(json_file_path)
    df.to_csv(csv_file_path, index=False)  
    return df 

def csv_to_json(csv_file_path, json_file_path):
    df = pd.read_csv(csv_file_path)
    df.to_json(json_file_path, orient='records', lines=True)
    return df

def overview(file_path):
    df = pd.read_csv(file_path)
    df['subcategory'] = df['subcategory'].fillna('')
    category_counts = df.groupby(['category', 'subcategory']).size().reset_index(name='count')
    print(category_counts)
    print("Total number of samples: ", len(df))
    
def sample_data(sample_size, input_file, output_file):
    print("Sampling of size: ", sample_size, " started, from file: ", input_file, " to file: ", output_file)
    df = pd.read_csv(input_file)
    df['subcategory'] = df['subcategory'].fillna('arithmetic_mixed')
    
    num_subcategories = df['subcategory'].nunique()
    print("Number of subcategories: ", num_subcategories)
    samples_per_subcategory = sample_size // num_subcategories

    sampled_df = pd.DataFrame()

    for subcategory in df['subcategory'].unique():
        sub_df = df[df['subcategory'] == subcategory]
        if len(sub_df) >= samples_per_subcategory:
            sampled_sub_df = sub_df.sample(n=samples_per_subcategory, random_state=1)
        else:
            # If there are not enough data points, take all available
            sampled_sub_df = sub_df
        sampled_df = pd.concat([sampled_df, sampled_sub_df])

    # Verify or adjust total samples if necessary
    if len(sampled_df) < sample_size:
        additional_samples = sample_size - len(sampled_df)
        extra_samples = df.sample(n=additional_samples, random_state=1)
        sampled_df = pd.concat([sampled_df, extra_samples])

    sampled_df.to_csv(output_file, index=False)
    
def load_rename_save(csv_file_path, output_csv_file_path):
    # Load the DataFrame from CSV
    df = pd.read_csv(csv_file_path)
    
    # Rename 'arithmetic-mixed' to 'arithmetic_mixed' in the 'subcategory' column
    df['subcategory'] = df['subcategory'].replace('arithmetic-mixed', 'arithmetic_mixed')
    
    # Save the updated DataFrame back to a CSV file
    df.to_csv(output_csv_file_path, index=False)


if __name__ == "__main__":
    generate_math401()
    print("Math401 generated")
    generate_mathematics_dataset()
    print("Mathematics Dataset generated")
    filter_out_non_numeric_answers("original-data-transformed/mathematics-dataset_transformed.json", "original-data-transformed/mathematics-dataset_transformed.json")
    merge_json_files("original-data-transformed/math401_transformed.json", "original-data-transformed/mathematics-dataset_transformed.json", "arithmetic_complete.json")
    print("Files merged")
    json_to_csv("arithmetic_complete.json", "arithmetic_complete.csv")
    print("Size of complete data: ", len(pd.read_csv("arithmetic_complete.csv")))
    sample_data(1000, "arithmetic_complete.csv", "arithmetic_1000.csv")
    print("Sample 1000, data generated")
    sample_data(100, "arithmetic_1000.csv", "arithmetic_100.csv")
    print("Sample 100, data generated")
    overview("arithmetic_100.csv")
    csv_to_json("arithmetic_1000.csv", "arithmetic_1000.json")
    print("Conversion of 1000 samples to JSON completed.")
    csv_to_json("arithmetic_100.csv", "arithmetic_100.json")
    print("Conversion of 100 samples to JSON completed.")
    overview("arithmetic_1000.csv")
    
    

