import torch 

class Agent(torch.nn.Module):
    def __init__(self):
        super(Agent, self).__init__()
        self.input = torch.nn.Linear(2, 50)
        self.hidden1 = torch.nn.Linear(50, 100)
        self.hidden2 = torch.nn.Linear(100,500)
        self.hidden3 = torch.nn.Linear(500, 100)
        self.hidden4 = torch.nn.Linear(100, 50)
        self.output = torch.nn.Linear(50,4)

    def forward(self, x):
        out = self.input(x)
        out = self.hidden1(out)
        out = self.hidden2(out)
        out = self.hidden3(out)
        out = self.hidden4(out)
        out = self.output(out)

        index = torch.argmax(out)

        return index

    