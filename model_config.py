MODEL_HOST = "huggingface"
# MODEL_HOST = "openai"

# Pick an OpenAI model:
OPENAI_MODEL = "gpt-4"

# Pick a base model hosted on HuggingFace:
BASE_MODEL_NAME = "Phind/Phind-CodeLlama-34B-v2"
BASE_MODEL_NAME = "Phind/Phind-CodeLlama-34B-Python-v1"
BASE_MODEL_NAME = "bigcode/starcoder"
# BASE_MODEL_NAME = "codellama/CodeLlama-34b-hf"
# BASE_MODEL_NAME = "codellama/CodeLlama-34b-Instruct-hf"
# BASE_MODEL_NAME = "deepseek-ai/deepseek-coder-33b-base"
# BASE_MODEL_NAME = "deepseek-ai/deepseek-coder-33b-instruct"
# BASE_MODEL_NAME = "mistralai/Mixtral-8x7B-Instruct-v0.1"

# Provide an optional checkpoint on top of the base model:
PEFT_MODEL_PATH = None

# Or pick an entire PPO model -- overrides all the above:
PPO_MODEL_PATH = "./my_ppo_model"

# Set to None for run.py to instead use base model (and optional peft):
PPO_MODEL_PATH = None

# Set to True to use custom stop words:
CUSTOM_STOP = False

# Set to True to use beam search instead of sampling
BEAM_SEARCH = False
