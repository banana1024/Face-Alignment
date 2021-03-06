import torch
from torch import nn

class LinearLoss(nn.Module):
    def __init__(self):
        super(LinearLoss, self).__init__()
    def forward(self, landmark_gt, landmarks, train_batchsize):
        l2_distant = torch.sum((landmark_gt - landmarks) * (landmark_gt - landmarks), axis=1)
        return torch.mean(l2_distant)