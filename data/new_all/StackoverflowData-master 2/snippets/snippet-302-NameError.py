#Source: https://stackoverflow.com/questions/61769186/h2otypeerror-training-frame-must-be-a-valid-h2oframe
gbm = h2o.get_model(sorted_final_grid.sorted_metric_table()['model_ids'][0])

params = gbm.params
new_params = {"nfolds":5, "model_id":None}
for key in new_params.keys():
    params[key]['actual'] = new_params[key] 
gbm_best = H2OGradientBoostingEstimator()
for key in params.keys():
    if key in dir(gbm_best) and getattr(gbm_best,key) != params[key]['actual']:
        setattr(gbm_best,key,params[key]['actual'])