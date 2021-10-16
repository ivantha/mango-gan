rm -rf trained_models
mkdir trained_models
python train_LFLSeg.py --train ../dataset/lflseg_train.txt --test ../dataset/lflseg_train.txt
