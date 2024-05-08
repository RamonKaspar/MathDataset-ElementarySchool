import json
import os
import matplotlib.pyplot as plt
import pandas as pd

def generate_MathQA_Geometry():
    filepath = "original-data/mathqa_geometry.json"
    outputpath = "original-data-transformed/mathqa_geometry_transformed.json"
    
    output_data = []
    
    with open(filepath, 'r', encoding='utf-8') as file:
        data = json.load(file)
        instances = data["Instances"]
        
        for entry in instances:
            try:
                answer = float(entry["Output Answer"][0])  
            except ValueError:
                print("Error: Invalid response value: ", entry["response"])
                
            transformed_data = {
                        "category": "Geometry",
                        "subcategory": "geometry",
                        "question": str(entry["Input"]),
                        "answer": answer,
                        "reasoning": str(entry["Output Program"][0]),
                        "source": "MathQA_Geometry"
                        }
            
            output_data.append(transformed_data)

    with open(outputpath, 'w', encoding='utf-8') as outfile:
        json.dump(output_data, outfile, indent=4, ensure_ascii=False) 

        
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
    generate_MathQA_Geometry()
    json_to_csv("original-data-transformed/mathqa_geometry_transformed.json", "geometry_complete.csv")
    overview("geometry_complete.csv")
    csv_to_json("geometry_complete.csv", "geometry_complete.json")
    sample_data(1000, "geometry_complete.csv", "geometry_1000.csv")
    csv_to_json("geometry_1000.csv", "geometry_1000.json")
    overview("geometry_1000.csv")
    sample_data(100, "geometry_1000.csv", "geometry_100.csv")
    csv_to_json("geometry_100.csv", "geometry_100.json")
    overview("geometry_100.csv")
    