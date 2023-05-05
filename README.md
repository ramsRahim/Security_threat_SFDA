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

- Please manually download the datasets [Office](https://drive.google.com/file/d/0B4IapRTv9pJ1WGZVd1VDMmhwdlE/view), [Office-Home](https://drive.google.com/file/d/0B81rNlvomiwed0V1YUxQdC1uOTg/view), [VisDA-C](https://github.com/VisionLearningGroup/taskcv-2017-public/tree/master/classification), [Office-Caltech](http://www.vision.caltech.edu/Image_Datasets/Caltech256/256_ObjectCategories.tar) from the official websites, and modify the path of images in each '.txt' under the folder './object/data/'. [**How to generate such txt files could be found in https://github.com/tim-learn/Generate_list **]

- Concerning the **Digits** dsatasets, the code will automatically download three digit datasets (i.e., MNIST, USPS, and SVHN) in './digit/data/'.    


### run the following command to train the source model with backdoor attack    
```py
python train_source.py --dset=office-home --max_epoch=100 --attack_type=badnet --device=cuda:0 --s=0
```

### run the following command to train the target model and see if the trojan transfers to the target model    
```py
python train_target.py --dset=office-home --max_epoch=15 --attack_type=badnet --device=cuda:0 --s=0
```