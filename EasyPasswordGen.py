#!/bin/python3
import random


#======================================================================================
#  ______                _____                                    _  _____            #              
# |  ____|              |  __ \                                  | |/ ____|           #              2022 Copyright (c) qweryy-dev
# | |__   __ _ ___ _   _| |__) |_ _ ___ _____      _____  _ __ __| | |  __  ___ _ __  #              2021 Copyright (c) EasyPasswordGen
# |  __| / _` / __| | | |  ___/ _` / __/ __\ \ /\ / / _ \| '__/ _` | | |_ |/ _ \ '_ \ #              All rights reserved
# | |___| (_| \__ \ |_| | |  | (_| \__ \__ \\ V  V / (_) | | | (_| | |__| |  __/ | | |#
# |______\__,_|___/\__, |_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_|\_____|\___|_| |_|#
#                   __/ |                                                             #
#                  |___/                                                              #
#======================================================================================


chars = 'qwertyuiopasdfghjklzxcvbnm123456789#@?!-_*'

length = input('password length?')
length = int(length)

for p in range(10):
  password =  ''
  for c in range(length):
    password += random.choice(chars)
  print(password)


print ("Thanks for using!")
