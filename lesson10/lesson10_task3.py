import random
from typing import Union


class TVController:

    def __init__(self, channels: list):
        self.channels = channels
        self.current_channel_cls: str = channels[0]
        self.volume: int = 10
        self.charge: Battery = Battery()

    def volume_up(self, quantity: int):
        self.charge.discharge()
        total_volume = self.volume + quantity
        if total_volume > 100:
            self.volume = 100
        else:
            self.volume = total_volume

    def volume_down(self, quantity: int):
        self.charge.discharge()
        total_volume = self.volume - quantity
        if total_volume < 0:
            self.volume = 0
        else:
            self.volume = total_volume

    def first_channel(self) -> str:
        self.charge.discharge()
        return f'"{self.channels[0]}"'

    def last_channel(self) -> str:
        self.charge.discharge()
        return f'"{self.channels[-1]}"'

    def turn_channel(self, n: int):
        self.charge.discharge()
        try:
            self.current_channel_cls = self.channels[n - 1]
            print(f'"{self.current_channel_cls}"')
        except IndexError:
            print(f'There is no such channel. You have only {len(self.channels)} channels')

    def next_channel(self):
        self.charge.discharge()
        try:
            index_channel: int = self.channels.index(f'{self.current_channel_cls}')
            self.current_channel_cls = self.channels[index_channel + 1]
            print(f'"{self.current_channel_cls}"')
        except IndexError:
            self.current_channel_cls = self.channels[0]
            print(f'"{self.current_channel_cls}"')

    def previous_channel(self):
        self.charge.discharge()
        try:
            index_channel: int = self.channels.index(f'{self.current_channel_cls}')
            self.current_channel_cls = self.channels[index_channel - 1]
            print(f'"{self.current_channel_cls}"')
        except IndexError:
            self.current_channel_cls = self.channels[-1]
            print(f'"{self.current_channel_cls}"')

    def current_channel(self):
        self.charge.discharge()
        print(f'"{self.current_channel_cls}"')

    def is_exist(self, n: Union[str, int]):
        if isinstance(n, int):
            if n > len(self.channels):
                print("No")
            else:
                print("Yes")
        elif isinstance(n, str):
            self.channels = [x.lower() for x in self.channels]
            if n.lower() in self.channels:
                print("Yes")
            else:
                print("No")

    def print_1(self):
        print(self.channels)


class Battery:  # type: ignore
    def __init__(self):
        self.charge_level = 100

    def discharge(self):
        new_charge_level = random.randint(self.charge_level - 10, self.charge_level - 1)
        if new_charge_level > 0:
            self.charge_level = new_charge_level
        else:
            raise Exception('Battery has run out of charge. Please put new one.')


CHANNELS = ["BBS", "Discovery", "TV1000"]
controller = TVController(CHANNELS)

# controller.volume_down(10)
# controller.volume_down(10)
# controller.volume_down(10)
# print(controller.volume)
# print(controller.charge.charge_level)

# import unittest
#
#
# class TestController(unittest.TestCase):
#
#     def test_first_channel(self):
#         some_TV = TVController(CHANNELS)
#         self.assertEqual('BBS', some_TV.first_channel(), "Wrong channel")
#
#     # def test_isupper(self):
#     #     self.assertTrue('FOO'.isupper())
#     #     self.assertFalse('Foo'.isupper())
#     #
#     # def test_split(self):
#     #     s = 'hello world'
#     #     self.assertEqual(s.split(), ['hello', 'world'])
#     #     # check that s.split fails when the separator is not a string
#     #     with self.assertRaises(TypeError):
#     #         s.split(2)
#
#
# if __name__ == '__main__':
#     unittest.main()