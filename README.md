# sWords-annotator

## Table of Contents

- [Project Description](#project-description)
- [Utilities](#utilities)
- [Usage](#usage)
- [File Structure](#file-structure)
- [License](#license)


## Project Description

The project aims to assist in the automatic annotation of data. By utilizing ChatGPT's natural language processing capabilities, the project aims to streamline the data annotation process (which is a type of keyword extraction task) and, thereby, increase efficiency.

The main features of the project include:

- **Data Processing**: The project includes a `DataProcessor` class that handles the input data, simplifies the dataset, and prepares it for annotation.
- **Prompt Generation**: The processed data is transformed into prompt entries that are suitable for input to ChatGPT.
- **Dialogue Interactions**: The project incorporates an initial (customizable) dialogue with ChatGPT to establish the system role and provide context for the subsequent prompt entries.
- **Batch Processing**: To handle large volumes of data, the project processes prompt entries in batches, ensuring that no data is lost and each batch stays within the token limit.

## Utilities

### DataProcessor Class

The `DataProcessor` class handles the processing of input data for annotation. It provides means to simplify the dataset and convert it into prompt entries suitable for ChatGPT.

#### Initialization

To initialize the `DataProcessor` class, provide the path to the input file:

```
from utils import DataProcessor

input_path = "path/to/input/file.csv"
data_processor = DataProcessor(input_path)
```

#### simplify_df Method

The `simplify_df` method simplifies the input dataframe by selecting relevant columns and saves it to the specified output path:

```
output_path = "path/to/output/simplified_df.csv"
simplified_df = data_processor.simplify_df(output_path)
```

#### csv2prompt Method

The `csv2prompt` method converts the input dataframe to prompt entries by extracting specific columns, saves the entries as both CSV and TXT files, and returns the extracted rows:

```
output_path = "path/to/output/prompt_entries"
extracted_rows = data_processor.csv2prompt(output_path)
```

### DataReader Class

The `DataReader` class provides utility methods for reading files.

#### read_file Method

The `read_file` method reads the content of a file and returns it as a string:

```
file_path = "path/to/file.txt"
content = DataReader.read_file(file_path)
```

#### read_lines Method

The `read_lines` method reads the content of a file and returns it as a list of lines:

```
file_path = "path/to/file.txt"
lines = DataReader.read_lines(file_path)
```

### CostCalculator Class

The `CostCalculator` class calculates the cost of tokens used in the ChatGPT API response.

#### Initialization

To initialize the `CostCalculator` class, provide the response from the ChatGPT API:

```
response = {
    # ChatGPT API response data
}
cost_calculator = CostCalculator(response)
```

#### calculate_input_tokens Method

The `calculate_input_tokens` method calculates the total input tokens used.

```
input_tokens = cost_calculator.calculate_input_tokens()
```

#### calculate_output_tokens Method

The `calculate_output_tokens` method calculates the total output tokens used.

```
output_tokens = cost_calculator.calculate_output_tokens()
```

#### calculate_input_cost Method

The `calculate_input_cost` method calculates the cost of input tokens.

```
input_cost = cost_calculator.calculate_input_cost()
```

#### calculate_output_cost Method

The `calculate_output_cost` method calculates the cost of output tokens.

```
output_cost = cost_calculator.calculate_output_cost()
```

#### calculate_total_cost Method

The `calculate_total_cost` method calculates the total cost of input and output tokens.

```
total_cost = cost_calculator.calculate_total_cost()
```

#### print_cost_information Method

The `print_cost_information` method prints the detailed cost information.

```
cost_calculator.print_cost_information()
```

## Usage

To use the `main.py` script, follow these steps:

1. Set up the necessary dependencies and environment. Make sure you have the required Python packages installed. You may need to install the `openai` package using pip:

```
!pip install openai
```

2. Set the API key for the OpenAI ChatGPT API. In the `main.py` script, locate the line:

```
openai.api_key = "YOUR-API-KEY"
```

3. Specify the input and output file paths. In the `main.py` script, locate the section:

```
in_path2raw_df = Paths.RAW_DATA
out_path4simplified_df = Paths.SIMPLIFIED_DF
out_path4prompts = Paths.PROMPT_ENTRIES
out_path4keymeanings = Paths.KEY_MEANINGS
out_path4sourcelines = Paths.SOURCE_LINES
```
The `config.py` is currently configured to the present directory structure in the repository. So a new source files should be uploaded to source/raw/ and the path should be changed accordingly in `config.py`. Alternatively, you can update the file paths and directory structure according to your directory structure and file names via `config.py`.

4. Run the `main.py` script. You can execute the script using your terminal or your desired IDE.


The script will perform the following actions:

- Process the raw data by simplifying the dataframe and saving it to the specified output path.
- Generate prompt entries and save them to the specified output path.
- Conduct an initial interaction with the ChatGPT model where the task is explained along with examples.
- Split the prompt entries into batches and send them to the ChatGPT API.
- Save the key meanings and source lines obtained from the API response to separate files.
- Print the cost information for the API usage.

**Make sure to customize the file paths and other configurations according to your specific project requirements.**

## File structure

Here, the crucial location is `project/source/raw` as this is the only input file that needs to be given by the user. Other files are generated by the programme for the purposes further processing.

```
project/
├── main.py
├── config.py
├── utils.py
│
├── source/
│   ├── raw/
│   │   └── StarWords words for Berke - words.csv
│   └── gpt_source/
│       ├── pl2en_simplified_entries.csv
│       └── gpt_entries.txt
|       └── gpt_entries.csv
└── target/
    ├── gpt_key_meanings/
    │   ├── KM-Batch0.txt
    |   ├── SP-Batch0.txt
    │   ├── KM-Batch1.txt
    |   ├── SP-Batch1.txt
    │   └── ...

```

## License

The project is licensed under the [MIT License](LICENSE).
