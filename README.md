# DataFlow models

Model files that the DataFlow desktop app downloads when someone asks for them. Each is checked
against the SHA-256 below before the app uses it, and runs only on the user's own computer.

## Decider 0.8B, personal-data check (`decider-0.8b-v1`)

| | |
|---|---|
| File | `decider-0.8b-Q8_0.gguf` (811,843,136 bytes) |
| SHA-256 | `6cba195228e7c01196cebfdd758c70a6cbf4672fe3247469b2a53cd343aaa7b7` |
| Source | [Mapika/decider-0.8b](https://huggingface.co/Mapika/decider-0.8b), revision `a0a01d6f8135298f400a8c856b355793012ae971` |
| Base model | [Qwen/Qwen3.5-0.8B-Base](https://huggingface.co/Qwen/Qwen3.5-0.8B-Base) |
| Licence | Apache License 2.0 ([LICENSE-decider](LICENSE-decider)), as the source and base model |

**Changes:** converted to GGUF with 8-bit (Q8_0) weights, without the multi-token prediction
layer the checkpoint's configuration names but doesn't ship. The weights are otherwise unchanged.
Made with `convert_hf_to_gguf.py --no-mtp --outtype q8_0` from the llama.cpp version bundled in
the `llama-cpp-sys-2` 0.1.160 Rust crate.

## multilingual-e5-small, recode suggestions (`multilingual-e5-small-v1`)

| | |
|---|---|
| File | `multilingual-e5-small-f16.gguf` (242,360,416 bytes) |
| SHA-256 | `527845993140bc735563f7ea3b09952fd460afaebd9bb11e2f55ba54a71120c5` |
| Source | [intfloat/multilingual-e5-small](https://huggingface.co/intfloat/multilingual-e5-small), revision `614241f622f53c4eeff9890bdc4f31cfecc418b3` |
| Licence | MIT ([LICENSE-multilingual-e5-small](LICENSE-multilingual-e5-small)) |

**Changes:** converted to GGUF with 16-bit weights, otherwise unchanged. The model has BERT
weights with an XLM-RoBERTa (sentencepiece) tokenizer, which the stock converter doesn't read
together; [convert/convert_e5.py](convert/convert_e5.py) runs `convert_hf_to_gguf.py --outtype f16`
with the XLM-RoBERTa tokenizer reader (same llama.cpp version as above).

DataFlow is made by ARCED International.
