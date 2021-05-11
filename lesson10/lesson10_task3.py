class TVController:
    channels = None
    current_channel_cls = None

    def __init__(self, channels):
        self.channels = channels
        self.current_channel_cls = channels[0]

    def first_channel(self):
        print(f'"{self.channels[0]}"')

    def last_channel(self):
        print(f'"{self.channels[-1]}"')

    def turn_channel(self, n):
        try:
            self.current_channel_cls = self.channels[n - 1]
            print(f'"{self.current_channel_cls}"')
        except IndexError:
            print(f'There is no such channel. You have only {len(self.channels)} channels')

    def next_channel(self):
        try:
            index_channel = self.channels.index(f'{self.current_channel_cls}')
            self.current_channel_cls = self.channels[index_channel + 1]
            print(f'"{self.current_channel_cls}"')
        except IndexError:
            self.current_channel_cls = self.channels[0]
            print(f'"{self.current_channel_cls}"')

    def previous_channel(self):
        try:
            index_channel = self.channels.index(f'{self.current_channel_cls}')
            self.current_channel_cls = self.channels[index_channel - 1]
            print(f'"{self.current_channel_cls}"')
        except IndexError:
            self.current_channel_cls = self.channels[-1]
            print(f'"{self.current_channel_cls}"')

    def current_channel(self):
        print(f'"{self.current_channel_cls}"')

    def is_exist(self, n):
        if type(n) == int:
            if n > len(self.channels):
                print("No")
            else:
                print("Yes")
        else:
            self.channels = [x.lower() for x in self.channels]
            if n.lower() in self.channels:
                print("Yes")
            else:
                print("No")

    def print_1(self):
        print(self.channels)


CHANNELS = ["BBS", "Discovery", "TV1000"]
controller = TVController(CHANNELS)