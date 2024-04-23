from langchain_core.language_models import BaseChatModel
from langchain_core.pydantic_v1 import root_validator, Field
from langchain_core.messages import BaseMessage, AIMessage
from langchain_core.outputs import ChatGeneration, ChatResult
from typing import Any, Dict, List, Optional

from mlx_lm import load as mlx_load
from mlx_lm import generate as mlx_generate

class MLXChatModel (BaseChatModel) :
    mlx_path: str
    mlx_model: Any = Field(default = None, exclude = True)
    mlx_tokenizer: Any = Field(default = None, exclude = True)
    max_tokens: int = Field(default = 250)

    @property
    def _llm_type(self) -> str:
        return 'MLXChatModel'

    @root_validator
    def load_model(cls, values: Dict) -> Dict:
        
        # Loading the model and tokenizer with the input string
        model, tokenizer = mlx_load(path_or_hf_repo=values['mlx_path'])

        # Saving the variables back appropriately
        values['mlx_model'] = model
        values['mlx_tokenizer'] = tokenizer

        return values
    
    def _generate(self, messages: List[BaseMessage], stop: Optional[List[str]]) -> ChatResult:
        prompt = '''
        You are a helpful AI assistant.
        
        '''

        for message in messages:
            prompt += f'\n\n{message.content}'

        mlx_response = mlx_generate(
            model = self.mlx_model,
            tokenizer = self.mlx_tokenizer,
            max_tokens = self.max_tokens,
            prompt = prompt
        )

        return ChatResult(generations= [ChatGeneration(message = AIMessage(content = mlx_response))])

