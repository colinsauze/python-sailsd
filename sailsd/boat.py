import socket

from .sailsd import Sailsd

class Boat(object):
    attrs = (
              'latitude',
              'longitude',
              'heading',
              'rudder-angle',
              'sail-angle',
            )

    def __init__(self, sailsd=None):
        self.sailsd = sailsd or Sailsd()
        self.status = 'not connected'

        for a in self.attrs:
            setattr(self, a, 0)

        self.x = self.longitude
        self.y = self.latitude

        self.update()

    def update(self):
        '''Read attributes from sailsd and update values'''
        try:
            res = self.sailsd.request(*self.attrs)
        except socket.error:
            self.status = 'not connected'
        else:
            self.status = 'connected'
            for a in self.attrs:
                v = res.get(a)
                setattr(self, a, v)

            self.x = self.longitude
            self.y = self.latitude