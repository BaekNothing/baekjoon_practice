
from transformers import PreTrainedTokenizerFast
tokenizer = PreTrainedTokenizerFast.from_pretrained("skt/kogpt2-base-v2",
  bos_token='</s>', eos_token='</s>', unk_token='<unk>',
  pad_token='<pad>', mask_token='<mask>')
print(tokenizer.tokenize("Tokenizer : Ready [],/."))

import torch
from transformers import GPT2LMHeadModel
import os

if(os.path.exists("kogpt2_model_trained.bin")):
    model = torch.load("kogpt2_model_trained.bin")
else:
    exit(print("there is no model"));

text = " "
while(text != "") :
    text = input('텍스트를 입력하십시오\n')
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