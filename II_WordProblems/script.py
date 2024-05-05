import json
import os
import matplotlib.pyplot as plt
import pandas as pd

def generate_AddSub():
    filepath = "original-data/AddSub.json"
    outputpath = "original-data-transformed/AddSub_transformed.json"
    
    output_data = []
    
    with open(filepath, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for entry in data:
            try:
                answer = float(entry["lSolutions"][0])  
            except ValueError:
                print("Error: Invalid response value: ", entry["response"])
                
            transformed_data = {
                        "category": "Word Problems",
                        "subcategory": "add_sub",
                        "question": entry["sQuestion"],
                        "answer": answer,
                        "reasoning": entry["lEquations"][0],
                        "source": "AddSub"
                        }
            
            output_data.append(transformed_data)

    with open(outputpath, 'w', encoding='utf-8') as outfile:
        json.dump(output_data, outfile, indent=4, ensure_ascii=False) 

def generate_MultiArith():
    filepath = "original-data/MultiArith.json"
    outputpath = "original-data-transformed/MultiArith_transformed.json"
    
    output_data = []
    
    with open(filepath, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for entry in data:
            try:
                answer = float(entry["lSolutions"][0])  
            except ValueError:
                print("Error: Invalid response value: ", entry["response"])
                
            transformed_data = {
                        "category": "Word Problems",
                        "subcategory": "multi_step",
                        "question": entry["sQuestion"],
                        "answer": answer,
                        "reasoning": entry["lEquations"][0],
                        "source": "MultiArith"
                        }
            
            output_data.append(transformed_data)

    with open(outputpath, 'w', encoding='utf-8') as outfile:
        json.dump(output_data, outfile, indent=4, ensure_ascii=False) 
        
def generate_SVAMP():
    filepath = "original-data/SVAMP.json"
    outputpath = "original-data-transformed/SVAMP_transformed.json"
    
    output_data = []
    
    with open(filepath, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for entry in data:
            try:
                answer = float(entry["Answer"])  
            except ValueError:
                print("Error: Invalid response value: ", entry["Answer"])
                
            transformed_data = {
                        "category": "Word Problems",
                        "subcategory": "challenge",
                        "question": entry["Body"] + " " + entry["Question"],
                        "answer": answer,
                        "reasoning": entry["Equation"],
                        "source": "SVAMP"
                        }
            
            output_data.append(transformed_data)

    with open(outputpath, 'w', encoding='utf-8') as outfile:
        json.dump(output_data, outfile, indent=4, ensure_ascii=False) 
        
def merge_json_files(file1, file2, file3, output_file):
    with open(file1, 'r', encoding='utf-8') as f1:
        data1 = json.load(f1)
    with open(file2, 'r', encoding='utf-8') as f2:
        data2 = json.load(f2)
    with open(file3, 'r', encoding='utf-8') as f3:
        data3 = json.load(f3)
    combined_data = data1 + data2 + data3
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


if __name__ == "__main__":
    generate_AddSub()
    generate_MultiArith()
    generate_SVAMP()
    merge_json_files("original-data-transformed/AddSub_transformed.json", "original-data-transformed/MultiArith_transformed.json", "original-data-transformed/SVAMP_transformed.json", "wordProblems_complete.json")
    json_to_csv("wordProblems_complete.json", "wordProblems_complete.csv")
    overview("wordProblems_complete.csv")
    sample_data(1000, "wordProblems_complete.csv", "wordProblems_1000.csv")
    sample_data(100, "wordProblems_1000.csv", "wordProblems_100.csv")
    overview("wordProblems_1000.csv")
    overview("wordProblems_100.csv")
    csv_to_json("wordProblems_100.csv", "wordProblems_100.json")
    csv_to_json("wordProblems_1000.csv", "wordProblems_1000.json")