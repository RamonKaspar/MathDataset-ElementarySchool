import deepl
import os
from dotenv import load_dotenv
import pandas as pd

# Load DeepL API key from .env file
load_dotenv()


def translate_json_to_german(input_path, output_path):
    df = pd.read_csv(input_path)
    auth_key = os.getenv("DEEPL_API_KEY")
    translator = deepl.Translator(auth_key)
    df['question'] = df['question'].apply(lambda x: translator.translate_text(x, target_lang="DE").text)
    df.to_csv(output_path, index=False)
    
def csv_to_json(input_path, output_path):
    df = pd.read_csv(input_path)
    df.to_json(output_path, orient='records')

if __name__ == "__main__":
    # Translate to German
    input_path = "../data/I_Arithmetic/arithmetic_100.csv"
    output_path = "arithmetic_100_german.csv"
    translate_json_to_german(input_path, output_path)
    print("Dataset arithmetic_100 translated to German")
    input_path = "../data/I_Arithmetic/arithmetic_1000.csv"
    output_path = "arithmetic_1000_german.csv"
    translate_json_to_german(input_path, output_path)
    print("Dataset arithmetic_1000 translated to German")
    input_path = "../data/II_WordProblems/wordProblems_100.csv"
    output_path = "wordProblems_100_german.csv"
    translate_json_to_german(input_path, output_path)
    print("Dataset wordProblems_100 translated to German")
    input_path = "../data/II_WordProblems/wordProblems_1000.csv"
    output_path = "wordProblems_1000_german.csv"
    translate_json_to_german(input_path, output_path)
    print("Dataset wordProblems_1000 translated to German")
    input_path = "../data/III_Geometry/geometry_100.csv"
    output_path = "geometry_100_german.csv"
    translate_json_to_german(input_path, output_path)
    print("Dataset geometry_100 translated to German")
    input_path = "../data/III_Geometry/geometry_1000.csv"
    output_path = "geometry_1000_german.csv"
    translate_json_to_german(input_path, output_path)
    print("Dataset geometry_1000 translated to German")
    
    # Convert to json
    input_path = "arithmetic_100_german.csv"
    output_path = "arithmetic_100_german.json"
    csv_to_json(input_path, output_path)
    input_path = "arithmetic_1000_german.csv"
    output_path = "arithmetic_1000_german.json"
    csv_to_json(input_path, output_path)
    input_path = "wordProblems_100_german.csv"
    output_path = "wordProblems_100_german.json"
    csv_to_json(input_path, output_path)
    input_path = "wordProblems_1000_german.csv"
    output_path = "wordProblems_1000_german.json"
    csv_to_json(input_path, output_path)
    input_path = "geometry_100_german.csv"
    output_path = "geometry_100_german.json"
    csv_to_json(input_path, output_path)
    input_path = "geometry_1000_german.csv"
    output_path = "geometry_1000_german.json"
