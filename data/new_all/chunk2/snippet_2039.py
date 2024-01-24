# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67606204/pytorch-training-an-lstm-attributeerror-nonetype-object-has-no-attribute-c
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
checkpoint_dir = '/content/gdrive/MyDrive/Checkpoint_dir'
_l_(452010)
data_dir = './data'
_l_(452011)

epochs=5
_l_(452012)

def custom_train_part(config, checkpoint_dir=None, data_dir=None):
    _l_(452240)

    model = _c_(452020, _n_(452013, "LSTM", lambda: LSTM), _c_(452017, _n_(452014, "len", lambda: len), _a_(452016, _n_(452015, "True_IMF_df", lambda: True_IMF_df), "T")), _n_(452018, "config", lambda: config)["Hidden"], _n_(452019, "config", lambda: config)["Layers"], 1)
    _l_(452021)
    

    device = "cpu"
    _l_(452022)
    if _c_(452026, _a_(452025, _a_(452024, _n_(452023, "torch", lambda: torch), "cuda"), "is_available")):
        _l_(452038)

        device = "cuda:0"
        _l_(452027)
        if _c_(452031, _a_(452030, _a_(452029, _n_(452028, "torch", lambda: torch), "cuda"), "device_count")) > 1:
            _l_(452037)

            model = _c_(452035, _a_(452033, _n_(452032, "nn", lambda: nn), "DataParallel"), _n_(452034, "model", lambda: model))
            _l_(452036)
    _c_(452042, _a_(452040, _n_(452039, "model", lambda: model), "to"), _n_(452041, "device", lambda: device))
    _l_(452043)
    optimizer = _c_(452051, _a_(452046, _a_(452045, _n_(452044, "torch", lambda: torch), "optim"), "Adam"), _c_(452049, _a_(452048, _n_(452047, "model", lambda: model), "parameters")), lr=_n_(452050, "config", lambda: config)["lr"])
    _l_(452052)
    criterion = _c_(452055, _a_(452054, _n_(452053, "nn", lambda: nn), "MSELoss"))
    _l_(452056)

    if _n_(452057, "checkpoint_dir", lambda: checkpoint_dir):
        _l_(452077)

        model_state, optimizer_state = _c_(452065, _a_(452059, _n_(452058, "torch", lambda: torch), "load"), _c_(452064, _a_(452062, _a_(452061, _n_(452060, "os", lambda: os), "path"), "join"), _n_(452063, "checkpoint_dir", lambda: checkpoint_dir), "checkpoint"))
        _l_(452066)
        _c_(452070, _a_(452068, _n_(452067, "model", lambda: model), "load_state_dict"), _n_(452069, "model_state", lambda: model_state))
        _l_(452071)
        _c_(452075, _a_(452073, _n_(452072, "optimizer", lambda: optimizer), "load_state_dict"), _n_(452074, "optimizer_state", lambda: optimizer_state))
        _l_(452076)
    
    for e in _c_(452080, _n_(452078, "range", lambda: range), _n_(452079, "epochs", lambda: epochs)):
        _l_(452236)


        running_loss = 0.0
        _l_(452081)
        epoch_steps = 0
        _l_(452082)
        
        _c_(452085, _a_(452084, _n_(452083, "model", lambda: model), "train"))  # put model to training mode
        _l_(452086)  # put model to training mode
        x = _c_(452090, _a_(452088, _n_(452087, "x_hht_train", lambda: x_hht_train), "to"), _n_(452089, "device", lambda: device))
        _l_(452091)
        y = _c_(452095, _a_(452093, _n_(452092, "y_hht_train", lambda: y_hht_train), "to"), _n_(452094, "device", lambda: device))
        _l_(452096)

        scores = _c_(452099, _n_(452097, "model", lambda: model), _n_(452098, "x", lambda: x))
        _l_(452100)
        loss = _c_(452104, _n_(452101, "criterion", lambda: criterion), _n_(452102, "scores", lambda: scores), _n_(452103, "y_hht_train", lambda: y_hht_train))
        _l_(452105)
        _c_(452108, _a_(452107, _n_(452106, "optimizer", lambda: optimizer), "zero_grad"))
        _l_(452109)
        _c_(452112, _a_(452111, _n_(452110, "loss", lambda: loss), "backward"))
        _l_(452113)
        _c_(452116, _a_(452115, _n_(452114, "optimizer", lambda: optimizer), "step"))
        _l_(452117)

        running_loss += _c_(452120, _a_(452119, _n_(452118, "loss", lambda: loss), "item"))
        _l_(452121)
        _c_(452124, _n_(452122, "print", lambda: print), f"Running loss: {_n_(452123, 'running_loss', lambda: running_loss)}")
        _l_(452125)
        epoch_steps += 1
        _l_(452126)

        if _n_(452127, "e", lambda: e) % 5 == 0:
            _l_(452140)

            _c_(452135, _n_(452128, "print", lambda: print), f'Epoch: {_n_(452129, "e", lambda: e)}, loss = {_c_(452134, _a_(452133, _c_(452132, _a_(452131, _n_(452130, "loss", lambda: loss), "cpu")), "item"))}')
            _l_(452136)
            # check_accuracy(loader_val, model)
            _c_(452138, _n_(452137, 'print', lambda: print))
            _l_(452139)
    
        # Validation loss
        val_loss = 0.0
        _l_(452141)
        val_steps = 0
        _l_(452142)
        total = 0
        _l_(452143)
        correct = 0
        _l_(452144)
        
        with _c_(452147, _a_(452146, _n_(452145, 'torch', lambda: torch), 'no_grad')):
            _l_(452203)

            x = _c_(452151, _a_(452149, _n_(452148, 'x_hht_val', lambda: x_hht_val), 'to'), _n_(452150, 'device', lambda: device))  # move to device, e.g. GPU
            _l_(452152)  # move to device, e.g. GPU
            y = _c_(452156, _a_(452154, _n_(452153, 'y_hht_val', lambda: y_hht_val), 'to'), _n_(452155, 'device', lambda: device))
            _l_(452157)

            scores = _c_(452160, _n_(452158, 'model', lambda: model), _n_(452159, 'x', lambda: x))
            _l_(452161)
            scores = _c_(452164, _a_(452163, _n_(452162, 'scores', lambda: scores), 'cpu'))
            _l_(452165)
            y = _c_(452168, _a_(452167, _n_(452166, 'y', lambda: y), 'cpu'))
            _l_(452169)
            correct += _c_(452181, _a_(452180, _c_(452179, _a_(452178, (_c_(452173, _a_(452171, _n_(452170, 'np', lambda: np), 'sign'), _n_(452172, 'scores', lambda: scores)) == _c_(452177, _a_(452175, _n_(452174, 'np', lambda: np), 'sign'), _n_(452176, 'y', lambda: y))), 'sum')), 'item'))
            _l_(452182)
            _c_(452185, _n_(452183, 'print', lambda: print), f"Correct: {_n_(452184, 'correct', lambda: correct)}")
            _l_(452186)

            loss = _c_(452190, _n_(452187, "criterion", lambda: criterion), _n_(452188, "scores", lambda: scores), _n_(452189, "y", lambda: y))
            _l_(452191)
            _c_(452196, _n_(452192, "print", lambda: print), f"Val Loss: {_c_(452195, _a_(452194, _n_(452193, 'loss', lambda: loss), 'item'))}")
            _l_(452197)
            val_loss += _c_(452200, _a_(452199, _n_(452198, "loss", lambda: loss), "cpu"))
            _l_(452201)
            val_steps += 1
            _l_(452202)

        with _c_(452207, _a_(452205, _n_(452204, "tune", lambda: tune), "checkpoint_dir"), _n_(452206, "e", lambda: e)) as checkpoint_dir:
            _l_(452225)

            path = _c_(452212, _a_(452210, _a_(452209, _n_(452208, "os", lambda: os), "path"), "join"), _n_(452211, "checkpoint_dir", lambda: checkpoint_dir), "checkpoint")
            _l_(452213)
            _c_(452223, _a_(452215, _n_(452214, "torch", lambda: torch), "save"), (_c_(452218, _a_(452217, _n_(452216, "model", lambda: model), "state_dict")), _c_(452221, _a_(452220, _n_(452219, "optimizer", lambda: optimizer), "state_dict"))), _n_(452222, "path", lambda: path))
            _l_(452224)

        _c_(452234, _a_(452227, _n_(452226, "tune", lambda: tune), "report"), loss=(_n_(452228, "val_loss", lambda: val_loss) / _n_(452229, "val_steps", lambda: val_steps)), accuracy = _n_(452230, "correct", lambda: correct) / _c_(452233, _n_(452231, "len", lambda: len), _n_(452232, "y_hht_val", lambda: y_hht_val)))
        _l_(452235)
    _c_(452238, _n_(452237, "print", lambda: print), "Finished Training")
    _l_(452239)



config = {
    "lr": _c_(452243, _a_(452242, _n_(452241, "tune", lambda: tune), "loguniform"), 1e-6, 1e-1),
    "Layers": _c_(452250, _a_(452245, _n_(452244, "tune", lambda: tune), "sample_from"), lambda _: _c_(452249, _a_(452248, _a_(452247, _n_(452246, "np", lambda: np), "random"), "randint"), 1, 10)),
    "Hidden" : _c_(452257, _a_(452252, _n_(452251, "tune", lambda: tune), "sample_from"), lambda _: _c_(452256, _a_(452255, _a_(452254, _n_(452253, "np", lambda: np), "random"), "randint"), 2, 100))
}
_l_(452258)

scheduler = _c_(452260, _n_(452259, "ASHAScheduler", lambda: ASHAScheduler), metric="loss",
        mode="min",
        max_t=10,
        grace_period=1,
        reduction_factor=2)
_l_(452261)

reporter = _c_(452263, _n_(452262, "CLIReporter", lambda: CLIReporter), metric_columns=["loss", "accuracy", "training_iteration"]
)
_l_(452264)

result = _c_(452271, _a_(452266, _n_(452265, "tune", lambda: tune), "run"), _n_(452267, "custom_train_part", lambda: custom_train_part),
    resources_per_trial={"cpu": 4, "gpu": 1},
    config=_n_(452268, "config", lambda: config),
    num_samples=1,
    scheduler = _n_(452269, "scheduler", lambda: scheduler),
    progress_reporter=_n_(452270, "reporter", lambda: reporter)
)
_l_(452272)

_c_(452277, _n_(452273, "print", lambda: print), f"Results: {_c_(452276, _a_(452275, _n_(452274, 'result', lambda: result), 'get_best_config'), metric = 'loss', mode = 'min')}")
_l_(452278)

best_trial = _c_(452281, _a_(452280, _n_(452279, "result", lambda: result), "get_best_trial"), metric = "loss", mode = "min")
_l_(452282)

_c_(452288, _n_(452283, "print", lambda: print), _c_(452287, _a_(452284, "Best trial config: {}", "format"), _a_(452286, _n_(452285, "best_trial", lambda: best_trial), "config")))
_l_(452289)
_c_(452295, _n_(452290, "print", lambda: print), _c_(452294, _a_(452291, "Best trial final validation loss: {}", "format"), _a_(452293, _n_(452292, "best_trial", lambda: best_trial), "last_result")["loss"]))
_l_(452296)
_c_(452302, _n_(452297, "print", lambda: print), _c_(452301, _a_(452298, "Best trial final validation accuracy: {}", "format"), _a_(452300, _n_(452299, "best_trial", lambda: best_trial), "last_result")["accuracy"]))
_l_(452303)

##############################################################
#                       AFTER TUNNING                       #
##############################################################

best_trained_model = _c_(452313, _n_(452304, "LSTM", lambda: LSTM), _c_(452308, _n_(452305, "len", lambda: len), _a_(452307, _n_(452306, "True_IMF_df", lambda: True_IMF_df), "T")), _a_(452310, _n_(452309, "best_trial", lambda: best_trial), "config")["Hidden"], _a_(452312, _n_(452311, "best_trial", lambda: best_trial), "config")["Layers"], 1)
_l_(452314)
best_checkpoint_dir = _a_(452317, _a_(452316, _n_(452315, "best_trial", lambda: best_trial), "checkpoint"), "value")
_l_(452318)
model_state, optimizer_state = _c_(452326, _a_(452320, _n_(452319, "torch", lambda: torch), "load"), _c_(452325, _a_(452323, _a_(452322, _n_(452321, "os", lambda: os), "path"), "join"), _n_(452324, "best_checkpoint_dir", lambda: best_checkpoint_dir), "checkpoint"))
_l_(452327)
_c_(452331, _a_(452329, _n_(452328, "best_trained_model", lambda: best_trained_model), "load_state_dict"), _n_(452330, "model_state", lambda: model_state))
_l_(452332)