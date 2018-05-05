# -*- coding: utf-8 -*-
import sys


sys.stdout.write(reduce(lambda x,y:x+y,
                     [chr(int(i,16)) for i in
                      sys.stdin.readline().split()]))
