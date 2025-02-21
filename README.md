# btp
bayesian optimization first run details ->

ranges for each hyper parameter was ->
hidden_layer_one = 32
hidden_layer_two = [64 or 128]
dropout_one = [0.28, 0.35]
dropout_two = [0.3, 0.45]

no. of trials -> 60 


RMSE: 63.517100592174266
Correlation: 0.9985189775849186
MAE: 48.205995751790525
RAE: 0.3908631474239629
RRSE: 0.4237429098319912
MAPE: 18.341334939187025
R2: 0.820441946367117

hyper parameters -> {'hidden_layer_one': 32, 'hidden_layer_two': 64, 'dropout_one': 0.29656897407859595, 'dropout_two': 0.3708375304640949, 'batch_size': 512, 'epochs': 200}
MSE -> 779.2195060521004


bayesian optimization second run details ->

ranges for each hyper parameter was ->
hidden_layer_one = 32
hidden_layer_two = [64 or 128]
dropout_one = [0.28, 0.35]
dropout_two = [0.11, 0.23]

no. of trials -> 65


RMSE: 39.37697984278187
Correlation: 0.9936337240731901
MAE: 31.10792290660915
RAE: 0.2522288040621508
RRSE: 0.26269643707622015
MAPE: 23.364014234895137
R2: 0.9309905819474595

hyper parameters -> {'hidden_layer_one': 32, 'hidden_layer_two': 128, 'dropout_one': 0.29778666582173113, 'dropout_two': 0.1156354551254656, 'batch_size': 512, 'epochs': 200}
MSE -> 463.72700309891405