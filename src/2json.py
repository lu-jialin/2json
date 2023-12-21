#!/usr/bin/env python3
import sys,argparse,textwrap,ctypes
from functools import reduce
import json as jsonlib
import tomli
import tomli_w
toml_limits = [
	'null' ,
	'single value or single list' ,
	'bool key' ,
	'YAML refrence' ,
]
class tomllib :
	def loads(s:str) : return tomli.loads(s)
	def dumps(obj)   :
		try :
			dump = tomli_w.dumps(obj)
		except Exception :
			raise Exception("TOML" , textwrap.dedent(
				f'''
				Error when try to ouput TOML.
				If other formats is valid, maybe {toml_limits} in tree
				'''
			).replace('\n','').replace('\r',''))
		return dump
import yaml as yamllib

parser = argparse.ArgumentParser()

#Based on input is preffered
types = {
	'j' : {
		type : 'JSON' ,
		callable : [
			jsonlib.loads ,
			lambda s : print(jsonlib.dumps(s)) ,
		] ,
	} ,
	't' : {
		type : 'TOML' ,
		callable : [
			tomllib.loads ,
			lambda s : print(tomllib.dumps(s)) ,
		] ,
	} ,
	'y' : {
		type : 'YAML' ,
		callable : [
			yamllib.safe_load ,
			lambda s : print(yamllib.dump(s)) ,
		] ,
	} ,
	'p' : {
		type : 'Python print' ,
		callable : [
			lambda _ : (_ for _ in ()).throw(Exception('It is not recommended parsing python print')) ,
			print ,
		] ,
	} ,
}
for t in types :
	parser.add_argument(f"-{t}" , action="store_true" , help= f'''Input as {types[t][type]}.''')
	parser.add_argument(f"-{t.upper()}" , action="store_true" , help= f'''output as {types[t][type]}.''')
args = vars(parser.parse_args())

flag = set(types)
flag = [
	list(set(args) & flag) ,
	list(set(args) - flag) ,
]

i = list(filter(lambda t:args[t] , flag[0]))
o = list(filter(lambda t:args[t] , flag[1]))
for io in [i,o] :
	if len(io)>1 :
		raise Exception(
			f'''Multiple format specified : {[t for t in io if args[t]==True]}'''
		)

def json3toml3yaml(tree) :
	try :
		tree = jsonlib.loads(tree)
	except Exception as jsone :
		try :
			tree = tomllib.loads(tree)
		except Exception as tomle :
			try :
				tree = yamllib.safe_load(tree)
			except Exception as yamle :
				print(f'TOML : {tomle}' , file=sys.stderr)
				print(f'JSON : {jsone}' , file=sys.stderr)
				print(f'YAML : {yamle}' , file=sys.stderr)
				raise Exception('Format' , 'Details is on the top')
	return tree

i = types[i.pop()][callable][0] if len(i)>0 else json3toml3yaml
o = types[o.pop().lower()][callable][1] if len(o)>0 else types['j'][callable][1]

o(i(sys.stdin.read()))
