import daemon
from guiltyspark_thread import run

print('starting')

with daemon.DaemonContext():
    run()

print('we done')
