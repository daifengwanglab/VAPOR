from torch.utils.data import Dataset, DataLoader
import pandas as pd
import torch

class Dataset(Dataset):
    def __init__(self, data_path, header=None, transform=None):
        self.data = pd.read_csv(data_path, header=header).to_numpy()
        self.transform = transform

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        sample = self.data[idx, :]
        if self.transform:
            sample = self.transform(sample)
        return sample

def get_dataloader(data_path, batch_size, shuffle=True,  header=None, transform=None, return_input_dim = True):
    dataset = Dataset(data_path=data_path, header=header, transform=transform)
    input_dim = dataset.data.shape[1]
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=shuffle)
    if return_input_dim:
        return dataloader, input_dim
    else:
        return dataloader 

def load_checkpoint(checkpoint_path, model, device, optimizer=None):
    """
    Loads model state (and optimizer state) from a file.
    """
    checkpoint = torch.load(checkpoint_path, map_location=device)
    model.load_state_dict(checkpoint['model_state_dict'])
    if optimizer:
        optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
    return checkpoint.get('epoch', -1)  # Return the last completed epoch number, if available