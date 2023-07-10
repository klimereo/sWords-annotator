import pandas as pd

class DataProcessor:
    def __init__(self, input_path):
        """
        Initializes the DataProcessor class.

        Args:
            input_path (str): The path to the input file.

        """
        self.raw_df = pd.read_csv(input_path)

    def simplify_df(self, output_path):
        """
                Simplifies the input dataframe by selecting relevant columns and saves it to the specified output path.

                Args:
                    output_path (str): The path to save the simplified dataframe.

                Returns:
                    pd.DataFrame: The simplified dataframe.

        """

        print(f"The shape of input dataframe {self.raw_df.shape}")
        self.raw_df["language"].fillna("", inplace=True)
        relevant_columns = self.raw_df[["form", "meaning", "KEY-MEANING"]]
        print(f"The shape of altered input dataframe: {relevant_columns.shape}")
        relevant_columns.to_csv(output_path)
        return relevant_columns

    def csv2prompt(self, output_path):
        """
            Converts the input dataframe to prompt entries by extracting specific columns,
            saves the entries as both CSV and TXT files, and returns the extracted rows.

            Args:
                output_path (str): The path to save the prompt entries.

            Returns:
                list: The extracted rows.

        """

        print(f"The shape of input dataframe {self.raw_df.shape}")
        self.raw_df["language"].fillna("", inplace=True)
        relevant_columns = self.raw_df[["form", "meaning", "KEY-MEANING"]]
        print(f"The shape of altered input dataframe: {relevant_columns.shape}")
        gpt_df = pd.DataFrame(columns=['Extracted'])
        extracted_rows = []

        for index, row in relevant_columns.iterrows():
            child_form = row['form']
            parent_meaning = row['meaning']
            extracted_row = f"Child: {child_form}; Parent: {parent_meaning}"
            gpt_df.loc[index, 'Extracted'] = extracted_row
            extracted_rows.append(extracted_row)

        # Save as CSV
        csv_output_path = output_path + ".csv"
        gpt_df.to_csv(csv_output_path, index=False)
        print(f"The shape of prompt dataframe: {gpt_df.shape}")

        # Save as TXT
        txt_output_path = output_path + ".txt"
        with open(txt_output_path, 'w') as file:
            file.write('\n'.join(extracted_rows))

        return extracted_rows

class DataReader:
    @staticmethod
    def read_file(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
        return content

    @staticmethod
    def read_lines(file_path):
        with open(file_path, 'r') as file:
            content = file.readlines()
        return content

def print_interaction(header, user_prompt, assistant_response, print_len):
    print(f"{header}\nUSER: {user_prompt[:print_len]} ... ")
    print(f"ASSISTANT: {assistant_response[:print_len]} ... ")
    print("--------------------------")


class CostCalculator:
    def __init__(self, response):
        """
        Initializes the CostCalculator class.

        Args:
            response (dict): The response from the ChatGPT API.

        """
        self.response = response

    def calculate_input_tokens(self):
        """
              Calculates the total input tokens used.

              Returns:
                  int: The total input tokens used.

        """
        return self.response['usage']['total_tokens']

    def calculate_output_tokens(self):
        """
               Calculates the total output tokens used.

               Returns:
                   int: The total output tokens used.

        """
        return sum(len(message) for message in self.response['choices'][0]['message']['content'].split('\n'))

    def calculate_input_cost(self):
        """
             Calculates the cost of input tokens.

             Returns:
                 float: The cost of input tokens.

        """
        input_tokens = self.calculate_input_tokens()
        return input_tokens * 0.0015 / 1000

    def calculate_output_cost(self):
        output_tokens = self.calculate_output_tokens()
        return output_tokens * 0.002 / 1000

    def calculate_total_cost(self):
        input_cost = self.calculate_input_cost()
        output_cost = self.calculate_output_cost()
        return input_cost + output_cost

    def print_cost_information(self):
        input_tokens = self.calculate_input_tokens()
        output_tokens = self.calculate_output_tokens()
        input_cost = self.calculate_input_cost()
        output_cost = self.calculate_output_cost()
        total_cost = self.calculate_total_cost()

        print(f"Total Tokens Used (Input): {input_tokens}")
        print(f"Total Tokens Used (Output): {output_tokens}")
        print(f"Cost (Input): ${input_cost:.5f}")
        print(f"Cost (Output): ${output_cost:.5f}")
        print(f"Total Cost: ${total_cost:.5f}")
