url = "https://colab.research.google.com/github/haven-jeon/KoGPT2-chatbot/blob/master/KoGPT2_chatbot_pytorch.ipynb"
url += "https://github.com/haven-jeon/KoGPT2-chatbot"
url += "https://github.com/SKT-AI/KoGPT2"
url += "https://vision-oasis.tistory.com/7?category=900851"

from transformers import PreTrainedTokenizerFast
tokenizer = PreTrainedTokenizerFast.from_pretrained("skt/kogpt2-base-v2",
  bos_token='</s>', eos_token='</s>', unk_token='<unk>',
  pad_token='<pad>', mask_token='<mask>')
print(tokenizer.tokenize("안녕하세요. 한국어 GPT-2 입니다.😤:)l^o"))

import torch
from transformers import GPT2LMHeadModel
import os

if(os.path.exists("kogpt2_pytorch_model.bin")):
    model = GPT2LMHeadModel.from_pretrained("kogpt2_pytorch_model.bin")
else:
    model = GPT2LMHeadModel.from_pretrained('skt/kogpt2-base-v2')
text = '나는 더 성장하고 싶어요. 천천히 생각해보자.'
input_ids = tokenizer.encode(text, return_tensors='pt')
gen_ids = model.generate(input_ids,
                           max_length=170,
                           repetition_penalty=2.0,
                           pad_token_id=tokenizer.pad_token_id,
                           eos_token_id=tokenizer.eos_token_id,
                           bos_token_id=tokenizer.bos_token_id,
                           use_cache=True)
generated = tokenizer.decode(gen_ids[0])
print(generated)
torch.save(model.state_dict(), 'kogpt2_state_dict.bin')
torch.save(model, 'kogpt2_model.bin')
