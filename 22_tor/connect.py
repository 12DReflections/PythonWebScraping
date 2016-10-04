import sys

from stem.connection import connect

if __name__ == '__main__':
  controller = connect()

  if not controller:
    sys.exit(1)  # unable to get a connection

  print 'Tor is running version %s' % controller.get_version()
  controller.close()
