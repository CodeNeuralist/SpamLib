import torch
import torch.nn as nn

class RNNSpamClassifier(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(RNNSpamClassifier, self).__init__()
        self.hidden_size = hidden_size
        self.rnn = nn.LSTM(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        out, _ = self.rnn(x)
        out = self.fc(out[:, -1, :])  
        out = self.sigmoid(out)
        return out
