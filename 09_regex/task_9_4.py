# -*- coding: utf-8 -*-

'''
Задание 9.4

Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
имя файла, в котором находится вывод команды show

Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
* Interface
* IP-Address
* Status
* Protocol

Информация должна возвращаться в виде списка кортежей:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'up', 'up')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла sh_ip_int_br_2.txt.
'''

import re

result = []
def parse_ip_int_br(config):
	with open(config) as data:
		result = re.findall('(\S+) +(\S+) +\w+ +\w+ +(up|down|auto|\S+ \S+) +(\S+)\s', data.read())
	return result
'''
itogi = parse_ip_int_br('sh_ip_int_br_2.txt')
print (itogi)
f = open('brief2.txt', 'w')
for i in itogi:
	i = str(i)
	f.writelines(i)
f.close()
'''
