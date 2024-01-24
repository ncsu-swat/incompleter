# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70621634/typeerror-forward-got-an-unexpected-keyword-argument-input-ids
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
training_args = _c_(406106, _a_(406105, _n_(406104, "tr", lambda: tr), "TrainingArguments"), output_dir='/home/pc/1_Proj_hate_speech/results_roberta',          # output directory
    overwrite_output_dir = True,
    num_train_epochs=20,              # total number of training epochs
    per_device_train_batch_size=16,  # batch size per device during training
    per_device_eval_batch_size=32,   # batch size for evaluation
    learning_rate=2e-5,
    warmup_steps=1000,                # number of warmup steps for learning rate scheduler
    weight_decay=0.01,               # strength of weight decay
    logging_dir='./logs3',            # directory for storing logs
    logging_steps=1000,
    evaluation_strategy="epoch"
    ,save_strategy="epoch"
    ,load_best_model_at_end=True
)
_l_(406107)


trainer = _c_(406115, _a_(406109, _n_(406108, "tr", lambda: tr), "Trainer"), model=_n_(406110, "model", lambda: model),                         # the instantiated 🤗 Transformers model to be trained
    args=_n_(406111, "training_args", lambda: training_args),                  # training arguments, defined above
    train_dataset=_n_(406112, "train_data", lambda: train_data),         # training dataset
    eval_dataset=_n_(406113, "val_data", lambda: val_data),             # evaluation dataset
    compute_metrics=_n_(406114, "compute_metrics", lambda: compute_metrics)
)
_l_(406116)