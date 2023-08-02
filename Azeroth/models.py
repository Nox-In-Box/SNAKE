import torch 

class Agent(torch.nn.Module):
    def __init__(self):
        super(Agent, self).__init__()
        self.input = torch.nn.Linear(6, 64)
        self.hidden1 = torch.nn.Linear(64, 128)
        self.hidden2 = torch.nn.Linear(128,512)
        self.hidden3 = torch.nn.Linear(512, 128)
        self.hidden4 = torch.nn.Linear(128, 64)
        self.output = torch.nn.Linear(64,3)
        self.activation = torch.nn.Sigmoid()

    def forward(self, x):
        out = self.input(x)
        out = self.hidden1(out)
        out = self.hidden2(out)
        out = self.hidden3(out)
        out = self.hidden4(out)
        out = self.output(out)
        out = self.activation(out)


       # index = torch.argmax(out)

        return out

    