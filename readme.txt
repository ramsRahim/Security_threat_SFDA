# install the requirements from requirements.txt
pip -r requirements.txt

# run the following command to train the source model with backdoor attack
python train_source.py --dset=office-home --max_epoch=100 --attack_type=badnet --device=cuda:0 --s=0

# run the following command to train the target model and see if the trojan transfers to the target model
python train_target.py --dset=office-home --max_epoch=15 --attack_type=badnet --device=cuda:0 --s=0
