# sWords-annotator

## Project Description

The project aims to assist in the automatic annotation of data. By utilizing ChatGPT's natural language processing capabilities, the project aims to streamline the data annotation process (which is a type of keyword extraction task) and, thereby, increase efficiency.

The main features of the project include:

- **Data Processing**: The project includes a `DataProcessor` class that handles the input data, simplifies the dataset, and prepares it for annotation.
- **Prompt Generation**: The processed data is transformed into prompt entries that are suitable for input to ChatGPT.
- **Dialogue Interactions**: The project incorporates an initial (customizable) dialogue with ChatGPT to establish the system role and provide context for the subsequent prompt entries.
- **Batch Processing**: To handle large volumes of data, the project processes prompt entries in batches, ensuring that no data is lost and each batch stays within the token limit.

## Usage

### DataProcessor Class

The **DataProcessor** class handles the processing of input data for annotation. It provides means to simplify the dataset and convert it into prompt entries suitable for ChatGPT.

#### Initialization

To initialize the DataProcessor class, provide the path to the input file:

```
from utils import DataProcessor

input_path = "path/to/input/file.csv"
data_processor = DataProcessor(input_path)
```

#### simplify_df Method

The simplify_df method simplifies the input dataframe by selecting relevant columns and saves it to the specified output path.

```
output_path = "path/to/output/simplified_df.csv"
simplified_df = data_processor.simplify_df(output_path)
```
