"""convert_hf_to_gguf.py for multilingual-e5-small: BERT weights (positions from 0) with an
XLM-RoBERTa sentencepiece tokenizer, which the stock BertModel converter doesn't read."""
import runpy, sys
sys.path.insert(0, sys.argv.pop(1))  # the llama.cpp checkout
from conversion import bert
bert.BertModel.set_vocab = bert.XLMRobertaModel._xlmroberta_set_vocab
runpy.run_path(sys.path[0] + "/convert_hf_to_gguf.py", run_name="__main__")
