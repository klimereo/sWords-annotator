import openai
import time
from utils import DataProcessor, CostCalculator, DataReader, print_interaction
from config import Paths

openai.api_key = "YOUR-API-KEY"

# Specifying Input/Output File Paths

in_path2raw_df = Paths.RAW_DATA
out_path4simplified_df = Paths.SIMPLIFIED_DF
out_path4prompts = Paths.PROMPT_ENTRIES
out_path4keymeanings = Paths.KEY_MEANINGS
out_path4sourcelines = Paths.SOURCE_LINES


# Processing raw data
data_processor = DataProcessor(in_path2raw_df)

## Polish-English simplified dataframe
simplified_data = data_processor.simplify_df(out_path4simplified_df)
## Polish-English prompt entries
promptified_data = data_processor.csv2prompt(out_path4prompts)

# Initial dialogue
## System role definition
system_role = DataReader.read_file(
    '/home/berke/PycharmProjects/pythonProject/SW Neural/gpt/prompts/system_role_prompt.txt')
print(f"{system_role[:80]} ... ")
print("--------------------------")

## Interaction 1
U1 = DataReader.read_file('/home/berke/PycharmProjects/pythonProject/SW Neural/gpt/prompts/1USER_instruction.txt')
A1 = DataReader.read_file('/home/berke/PycharmProjects/pythonProject/SW Neural/gpt/prompts/1GPT_response.txt')
print_interaction("Interaction 1", U1, A1, 80)

## Interaction 2
U2 = DataReader.read_file('/home/berke/PycharmProjects/pythonProject/SW Neural/gpt/prompts/2USER_examples.txt')
A2 = DataReader.read_file('/home/berke/PycharmProjects/pythonProject/SW Neural/gpt/prompts/2GPT_understanding.txt')
print_interaction("Interaction 2", U2, A2, 80)

## Interaction 3
U3 = DataReader.read_file('/home/berke/PycharmProjects/pythonProject/SW Neural/gpt/prompts/3USER_trials.txt')
A3 = DataReader.read_file('/home/berke/PycharmProjects/pythonProject/SW Neural/gpt/prompts/3GPT_answers.txt')
print_interaction("Interaction 3", U3, A3, 80)

## Interaction 4
U4 = DataReader.read_file('/home/berke/PycharmProjects/pythonProject/SW Neural/gpt/prompts/4USER_approval.txt')
A4 = DataReader.read_file('/home/berke/PycharmProjects/pythonProject/SW Neural/gpt/prompts/4GPT_ready.txt')
print_interaction("Interaction 4", U4, A4, 80)

# Prompt entries

## Make sure that a batch + dialogue does not exceed 4097 tokens
## 80 (data points) seems to be optimal. Exceeding beyond 100 is quite risky
batch_size = 80

path2prompts = out_path4prompts + ".txt"
lines = DataReader.read_lines(path2prompts)

# Split lines into batches
line_batches = [lines[i:i + batch_size] for i in range(0, len(lines), batch_size)]


for index, batch in enumerate(line_batches):
    start_time = time.time()
    # Join lines within the batch
    batch_str = ''.join(batch)
    # Root dialogue
    messages = [
        {"role": "system", "content": system_role},
        {"role": "user", "content": U1},
        {"role": "assistant", "content": A1},
        {"role": "user", "content": U2},
        {"role": "assistant", "content": A2},
        {"role": "user", "content": U3},
        {"role": "assistant", "content": A3},
        {"role": "user", "content": U4},
        {"role": "assistant", "content": A4},
        {"role": "user", "content": f"Here is {batch_size} entries:\n {batch_str}"}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    key_meanings = response['choices'][0]['message']['content']

    elapsed_time = time.time() - start_time
    print(f"It took {elapsed_time:.3f} seconds to compute {batch_size} lines.")
    print("-------------------------------------------")

    with open(f"{out_path4keymeanings}KM-Batch{index}.txt", 'w') as file:
        file.write(key_meanings)
    with open(f"{out_path4sourcelines}SP-Batch{index}.txt", 'w') as file:
        file.write(batch_str)

    # Retrieve and print the cost information
    cost_calculator = CostCalculator(response)
    cost_calculator.print_cost_information()

