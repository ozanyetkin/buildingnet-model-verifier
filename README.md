# buildingnet-model-verifier
Model verifier for [BuildingNet](https://buildingnet.org/) that eliminates non-available model entries in the dataset.

## Problem
When the BuildingNet dataset is downloaded by filling out the [form](https://docs.google.com/forms/d/e/1FAIpQLSevg7fWWMYYMd1vaOdDloUX_55VOQK7PqS1DlniFV7_vuoI0w/viewform), there are several versions available, yet it seems like some models are missing in `pretrained_avgpool_minkownormal_features`.

### Example
Running the following code as [BuildingNet repository](https://github.com/buildingnet/buildingnet_dataset) suggests:

```
python3 train.py --datadir="data" --epoch 200 --outputdir 'Output' --ckpt_dir 'checkpoint' --normalization 'GN' --modeltype 'Edge' --edgetype 'all' --lr 1e-4 --nodetype 'node+minkownormal' --pretrainedtype 'fc3_avg' --IOU_checkpoint=5
```

Throws the following error:
```
FileNotFoundError: [Errno 2] No such file or directory: 'data/pretrained_avgpool_minkownormal_features/fc3_avg/RESIDENTIALhouse_mesh1367.pth.tar'
```

## Solution
This script will verify the existence of the models in the dataset and eliminate the non-available ones from `test.txt`, `train.txt`, and `val.txt`.


## Usage
Simply run the following command to verify the existence of the models in the dataset, this will edit the `test.txt`, `train.txt`, and `val.txt` files accordingly:

```
python3 model_verifier.py
```

It looks for the models in the following directory, you can change it in the script if you have a different path:
```
models_path = "./pretrained_avgpool_minkownormal_features/fc3_avg"
```