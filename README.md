# Chatbot Demo with OpenAI GPT-3 Language Model API

Three components for this chatbot demo with openAI GPT-3 language model API:
 - OepnAI Language Model API
 - Frontend chatbot UI template
 - System configuration

## Step-by-step configuration
The following guideline is for linux, WSL2, or MacOS operating systems. 

 - clone this repository
 - change directory to `/config` and update the system variable `OPENAI_API_KEY` value in the `add_openai_api_key.sh` file
 - make sure the `add_openai_api_key.sh` file is executable by running the following command in terminal: 
    `chmod +x add_openai_api_key.sh`
 - execute the config shell script by running `./add_openai_api_key.sh`
 - validate the setup of creating an `OPENAI_API_KEY` system variable by `echo $OPENAI_API_KEY`

### without docker
 - create new conda environment with python 3.10 by running `conda create -n chatbot python=3.10` in the terminal.
 - in the `/app` directory where `main.py` file is, run `uvicorn app:main 




## Scope of Fine-Tuning and Prompt Engineering
- Fine-tuning with base models
- Embedding similarity + prompt engineering

Both fine-tuning and prompt engineering could improve the language model completion quality. Fine-tuning would update the language model parameters based on the training dataset while prompt engineering world provide additional context in the promot without modifying the pre-training language model. The key difference comparisons between fine-tuning and prompt engineering for the chatbot LLM use case are summarized in the following table:

| | Fine-tuning | Prompt engineering |
|----|----|----|
| Training data | Normally requires large amount of task-specific training data | Small amount task-specific context data required |
| Accuracy | Can achieve high accuracy with sufficient training data | May require careful tuning to achieve high accuracy |
| Resource Usage | Requires significant computational resources and time for training | Can be computationally efficient |
| Potential Issues | Catastrophic forgetting, generated non-factual content | Prompt length limit and more token consumption |



### Preparation of training dataset
Training data embedding reference creation and provide context information. 