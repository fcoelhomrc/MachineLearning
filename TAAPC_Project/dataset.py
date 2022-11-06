import torch
from torch.utils.data import Dataset
import tarfile, glob, os
from constants import TARFILE_PATH, DATA_PATH

def extract_tar(input_path, output_path="."):
    '''
    input_path: path to .tar data
    output_path: path where data will be extracted to
    '''
    with tarfile.open(input_path, "r") as f:
        f.extractall(output_path)

class MVTECDataset(Dataset):
    '''
    category - str: which class you want to load
    '''
    def __init__(self, main_path, category):
        self.path = os.path.join(main_path, category)
        print(self.path)
        self.load_data("train")

    def __len__(self):
        pass

    def __getitem__(self):
        pass

    def load_data(self, descriptor):
        assert descriptor in ["train", "test", "ground_truth"]
        path = os.path.join(self.path, descriptor) 
        for dir in os.listdir(path):
            for name in glob.glob(os.path.join(path, dir) + r"\*.png"):
                with open(name, "w") as f:
                    print(name)



if __name__ == "__main__":
    # extract_tar(TARFILE_PATH, DATA_PATH)
    cat = "capsule"
    test = MVTECDataset(DATA_PATH, cat)