class Paths:
    # Input Paths
    ## Raw data path (.csv version of the dataframe)
    RAW_DATA = "source/raw/StarWords words for Berke - words.csv"

    # Output paths (No need to modify unless needed for some reason)
    ## Simplified dataframe saving path (for output)
    SIMPLIFIED_DF = "source/gpt source/pl2en_simplified_entries.csv"

    ## Prompt entries saving path
    ### (without extension)
    PROMPT_ENTRIES = "source/gpt source/gpt_entries"
    ### without file name specification, only folder
    KEY_MEANINGS = "target/"
    SOURCE_LINES = "target/"
