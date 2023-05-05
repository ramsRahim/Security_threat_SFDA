# Security_threat_SFDA

### Prerequisites:
- python == 3.6.8
- pytorch ==1.1.0
- torchvision == 0.3.0
- numpy, scipy, sklearn, PIL, argparse, tqdm

### install the requirements from requirements.txt
```bash
pip -r requirements.txt
```
### Dataset:

- Please manually download the dataset [Office-Home](https://drive.google.com/file/d/0B81rNlvomiwed0V1YUxQdC1uOTg/view) from the official website, and modify the path of images in each '.txt' under the folder './data/'. [**How to generate such txt files could be found in https://github.com/tim-learn/Generate_list **]


### run the following command to train the source model with backdoor attack    
```bash
python train_source.py --dset=office-home --max_epoch=100 --attack_type=badnet --device=cuda:0 --s=0
```

### run the following command to train the target model and see if the trojan transfers to the target model    
```bash
python train_target.py --dset=office-home --max_epoch=15 --attack_type=badnet --device=cuda:0 --s=0
```
