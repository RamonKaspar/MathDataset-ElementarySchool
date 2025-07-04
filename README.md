# Math Dataset for elementary school grade

This repository is dedicated to compiling a comprehensive and balanced dataset tailored to match the mathematics curriculum for 10-year-olds. Our goal is to provide a robust resource that supports the development and evaluation of educational tools like chatbots, which can effectively answer math questions tailored to elementary students.

## Methodology

We followed a methodical approach to construct this dataset:

- **Classification of Math Questions:** We categorized questions to allow for targeted educational interventions and specialized solution techniques.

- **Search for Suitable Datasets:** We identified datasets for each category, ensuring they align with the learning level and content requirements of elementary school math.

- **Compilation and Sampling:** We combined and randomly sampled from exisitng datasets to create a diverse collection that accurately mirrors the types of math challenges faced by 10-year-olds.

## Categorization

Our dataset categorizes mathematical questions into three groups:

1. **Arithmetic:** Includes basic calculations, measurement conversions, and more. (E.g. "What is 1.20m in mm?" or "What is 12+8?")
2. **Word Problems:** Engages students with real-world scenarios requiring mathematical solutions. (E.g. "If you split 50$ equally among 5 people, how much does each get?")
3. **Geometry:** Focuses on shape, space, and measurement problems suitable for young learners. (E.g. "What is the volume of a sphere with radius 6 cm?")

These categories where inspired by [Ahn et al., 2024](https://arxiv.org/abs/2402.00157).

## Dataset Selection Criteria

We adhered to rigorous criteria to ensure the dataset's relevance and quality:

- Language: English-only to maintain consistency across data.
- Educational Level: Suitable for elementary school math levels.
- Content Type: Focused exclusively on text-based datasets, avoiding any that include pictures or additional multimedia sources to ensure straightforward analysis.
- Single Float Answer: The answer to each question is a single float value. This ensures easy evaluation.

# Dataset Overview

### Format

The dataset is a collection of `.json` objects. Each object has the following format:

```json
{
  "category": "Arithmetic | Word Problems | Gemoetry",
  "subcategory": "<divided category further>",
  "question": "<question>",
  "answer": "<answer as float>",
  "reasoning": "(optional) <can be an equation, python program, etc.>",
  "source": "<source dataset name>"
}
```

Example Entry (from the SVAMP dataset):

```json
{
  "category": "Word Problem",
  "subcategory": "challenge",
  "question": "Dan had $ 3 left with him after he bought a candy bar. If he had $ 4 at the start, how much did the candy bar cost?",
  "answer": 1.0,
  "reasoning": "( 4.0 - 3.0 )",
  "source": "SVAMP"
}
```

### Directory Structure & Data Management

The datasets are organized into three categories, with varying availability due to file size constraints:

**Available in Repository:**
- **Word Problems**: All versions (`wordProblems_complete`, `wordProblems_1000`, `wordProblems_100`) 
- **Geometry**: All versions (`geometry_complete`, `geometry_1000`, `geometry_100`)
- **Arithmetic**: Sample versions only (`arithmetic_1000`, `arithmetic_100`)

**Arithmetic Complete Dataset:**
The `arithmetic_complete` dataset is too large for GitHub (2.3GB). To recreate it:

1. Download source data:
   - **Mathematics Dataset**: https://console.cloud.google.com/storage/browser/mathematics-dataset
   - **Math-401**: https://github.com/GanjinZero/math401-llm

2. Run the processing script: `/data/I_Arithmetic/script.py`

The datasets are versioned into three types for each category:

- `<category>_complete.csv/json`: Provides the comprehensive dataset, ideal for extensive analysis.
- `<category>_1000.csv/json`: A balanced sample of 1000 items, perfect for in-depth testing.
- `<category>_100.csv/json`: A smaller sample of 100 items, designed for quick assessments.

All sample datasets (`<category>_1000.csv/json` and `<category>_100.csv/json`) are directly accessible within this repository in the data directory.

## Translation to German

We have utilized the `DeepL API` for high-quality, free translations of selected datasets into German. For access to the data and more details about the translation process, please visit the `translation-to-german` folder.

## Oerview of the different dataset versions

This table gives an overview of the different dataset versions.

| Section           | Name                    | Number of subcategories | Size      |
| ----------------- | ----------------------- | ----------------------- | --------- |
| I. Arithmetic     | `arithmetic_complete`   | 14                      | 7,731,654 |
|                   | `arithmetic_1000`       | 14                      | 1,000     |
|                   | `arithmetic_100`        | 14                      | 100       |
| II. Word Problems | `wordProblems_complete` | 3                       | 1,995     |
|                   | `wordProblems_1000`     | 3                       | 1,000     |
|                   | `wordProblems_100`      | 3                       | 100       |
| III. Geometry     | `geometry_complete`     | 1                       | 1,698     |
|                   | `geometry_1000`         | 1                       | 1,000     |
|                   | `geometry_100`          | 1                       | 100       |

## Exploring the Dataset

A nice overview of all available datasets in the mathematical domain can be found in [Lu et al, 2023](https://arxiv.org/abs/2212.10535) and in [Ahn et al., 2024](https://arxiv.org/abs/2402.00157).

In constructing this dataset, we made a concerted effort to include a comprehensive range of datasets that are best suited for the educational level and cognitive abilities of 10-year-olds. While we don't provide extensive details on the selection process for each dataset, our overarching goal was to incorporate as many relevant and suitable datasets as possible.

<table border="1" style="border-collapse: collapse; width: 100%;">
    <caption>Overview of the dataset. Here all versions with 1000 samples are listed.</caption>
    <thead>
        <tr>
            <th colspan="4"><h3>I. Arithmetic</h3></th>
        </tr>
    </thead>
    <thead>
        <tr>
            <th><strong>Source</strong></th>
            <th><strong>Subcategory</strong></th>
            <th><strong>Size</strong></th>
            <th><strong>Example</strong></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><a href="https://github.com/GanjinZero/math401-llm">Math-401</a></td>
            <td><code>arithmetic_mixed</code></td>
            <td>71</td>
            <td>log 10(797)=</td>
        </tr>
        <tr>
            <td rowspan="13"><a href="https://github.com/google-deepmind/mathematics_dataset">Mathematics Dataset (Google Deepmin)</a></td>
            <td><code>add_or_sub</code></td>
            <td>71</td>
            <td>What is -6.5 + -1.5?</td>
        </tr>
        <tr>
            <td><code>add_sub_multiple</code></td>
            <td>71</td>
            <td>Calculate -4 + 0 - ((-3 - -1) + 7).</td>
        </tr>
        <tr>
            <td><code>conversion</code></td>
            <td>71</td>
            <td>What is three eighths of a kilogram in grams?</td>
        </tr>
        <tr>
            <td><code>div</code></td>
            <td>71</td>
            <td>Calculate -238 divided by -3.</td>
        </tr>
        <tr>
            <td><code>div_remainder</code></td>
            <td>73</td>
            <td>What is the remainder when 255 is divided by 20?</td>
        </tr>
        <tr>
            <td><code>gcd</code></td>
            <td>72</td>
            <td>What is the highest common divisor of 75 and 390?</td>
        </tr>
        <tr>
            <td><code>lcm</code></td>
            <td>72</td>
            <td>Calculate the lowest common multiple of 1355 and 80.</td>
        </tr>
        <tr>
            <td><code>mul</code></td>
            <td>72</td>
            <td>Multiply -0.0756 and 0.14.</td>
        </tr>
        <tr>
            <td><code>mul_div_multiple</code></td>
            <td>71</td>
            <td>Evaluate 2/(-6)*(-120)/(-80).</td>
        </tr>
        <tr>
            <td><code>place_value</code></td>
            <td>71</td>
            <td>What is the tens digit of 5546?</td>
        </tr>
        <tr>
            <td><code>round_number</code></td>
            <td>71</td>
            <td>Round 4117.6 to the nearest 10.</td>
        </tr>
        <tr>
            <td><code>sequence_next_term</code></td>
            <td>72</td>
            <td>What comes next: -75, -80, -85, -90?</td>
        </tr>
        <tr>
            <td><code>time</code></td>
            <td>71</td>
            <td>How many minutes are there between 1:03 PM and 9:11 PM?</td>
        </tr>
    </tbody>
    <thead>
        <tr>
            <th colspan="4"><h3>II. Word Problems</h3></th>
        </tr>
    </thead>
    <thead>
        <tr>
            <th><strong>Source</strong></th>
            <th><strong>Subcategory</strong></th>
            <th><strong>Size</strong></th>
            <th><strong>Example</strong></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><a href="https://github.com/arkilpatel/SVAMP">SVAMP</a></td>
            <td><code>challenge</code></td>
            <td>334</td>
            <td>At the arcade Edward won 9 tickets. If he spent 4 tickets on a beanie and later won 4 more tickets, how many would he have?</td>
        </tr>
        <tr>
            <td><a href="https://github.com/wangxr14/Algebraic-Word-Problem-Solver/blob/master/data/AddSub.json">AddSub</a></td>
            <td><code>add_sub</code></td>
            <td>333</td>
            <td>Tim has 44 books. Sam has 52 books. How many books do they have together?</td>
        </tr>
        <tr>
            <td><a href="https://huggingface.co/datasets/ChilleD/MultiArith">MultiArith</a></td>
            <td><code>multi_step</code></td>
            <td>333</td>
            <td>Roger had 25 books. If he sold 21 of them and used the money he earned to buy 30 new books, how many books would Roger have?</td>
        </tr>
    </tbody>
    <thead>
        <tr>
            <th colspan="4"><h3>III. Geometry</h3></th>
        </tr>
    </thead>
    <thead>
        <tr>
            <th><strong>Source</strong></th>
            <th><strong>Subcategory</strong></th>
            <th><strong>Size</strong></th>
            <th><strong>Example</strong></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><a href="https://allenai.org/data/lila">MathQA Geometry</a></td>
            <td><code>geometry</code></td>
            <td>1000</td>
            <td>Find the surface area of a 8 cm x 6 cm x 2 cm brick</td>
        </tr>
    </tbody>
</table>

## References

Overview of existing datasets in the mathematical domain:

- P. Lu, L. Qiu, W. Yu, S. Welleck, and K.-W. Chang, “A Survey of Deep Learning for Mathematical Reasoning.” arXiv, Jun. 21, 2023. Accessed: May 02, 2024. [Online]. Available: http://arxiv.org/abs/2212.10535
- J. Ahn, R. Verma, R. Lou, D. Liu, R. Zhang, and W. Yin, “Large Language Models for Mathematical Reasoning: Progresses and Challenges.” arXiv, Apr. 05, 2024. doi: 10.48550/arXiv.2402.00157.
- W. Liu et al., “Mathematical Language Models: A Survey.” arXiv, Feb. 23, 2024. Accessed: May 02, 2024. [Online]. Available: http://arxiv.org/abs/2312.07622

References for the used datasets we sampled from:

- **[Math-401](https://github.com/GanjinZero/math401-llm)**: W. Liu et al., “Mathematical Language Models: A Survey.” arXiv, Feb. 23, 2024. Accessed: May 02, 2024. [Online]. Available: http://arxiv.org/abs/2312.07622
- **[Mathematics Dataset](https://github.com/google-deepmind/mathematics_dataset)**: D. Saxton, E. Grefenstette, F. Hill, and P. Kohli, “Analysing Mathematical Reasoning Abilities of Neural Models.” arXiv, Apr. 02, 2019. doi: 10.48550/arXiv.1904.01557.
- **[SVAMP](https://github.com/arkilpatel/SVAMP)**: A. Patel, S. Bhattamishra, and N. Goyal, “Are NLP Models really able to Solve Simple Math Word Problems?” arXiv, Apr. 15, 2021. doi: 10.48550/arXiv.2103.07191.
- **[AddSub](https://github.com/wangxr14/Algebraic-Word-Problem-Solver/blob/master/data/AddSub.json)**: M. J. Hosseini, H. Hajishirzi, O. Etzioni, and N. Kushman, “Learning to Solve Arithmetic Word Problems with Verb Categorization,” in Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP), A. Moschitti, B. Pang, and W. Daelemans, Eds., Doha, Qatar: Association for Computational Linguistics, Oct. 2014, pp. 523–533. doi: 10.3115/v1/D14-1058.
- **[MultiArith](https://huggingface.co/datasets/ChilleD/MultiArith)**: S. Roy and D. Roth, “Solving General Arithmetic Word Problems.” arXiv, Aug. 20, 2016. doi: 10.48550/arXiv.1608.01413.
- **[MathQA Geometry](https://allenai.org/data/lila)**: A. Amini, S. Gabriel, S. Lin, R. Koncel-Kedziorski, Y. Choi, and H. Hajishirzi, “MathQA: Towards Interpretable Math Word Problem Solving with Operation-Based Formalisms,” in Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers), J. Burstein, C. Doran, and T. Solorio, Eds., Minneapolis, Minnesota: Association for Computational Linguistics, Jun. 2019, pp. 2357–2367. doi: 10.18653/v1/N19-1245.
