class BrowserHistory:
    def __init__(self, homepage: str):
        self.urls = [homepage]
        self.index = 0
        
    def visit(self, url: str) -> None:
        self.urls = self.urls[:self.index+1] + [url]
        self.index+= 1

    def back(self, steps: int) -> str:
        self.index -= steps
        if self.index < 0:
            self.index = 0
            
        return self.urls[self.index]    
        
    def forward(self, steps: int) -> str:
        self.index += steps
        if self.index > len(self.urls) - 1:
            self.index = len(self.urls) - 1
        
        return self.urls[self.index]