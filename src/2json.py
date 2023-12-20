#!/bin/env python3
import sys,argparse
import tomli
import tomli_w
class tomllib :
	def loads(s:str) : return tomli.loads(s)
	def dumps(obj)   : return tomli_w.dumps(obj)
import json as jsonlib
import yaml as yamllib

toml_limits = [
	'null' ,
	'single value or single list' ,
	'YAML refrence' ,
]
parser = argparse.ArgumentParser()
parser.add_argument('-j' , action="store_true" , help= '''Input as JSON.''')
parser.add_argument('-t' , action="store_true" , help= '''Input as TOML.''')
parser.add_argument('-y' , action="store_true" , help= '''Input as YAML.''')

parser.add_argument('-J' , action="store_true" , help='Output as JSON(default)')
parser.add_argument('-T' ,  action="store_true" , help=
f'''
Output as TOML.
Note that {toml_limits} is not supported in TOML.
'''
)
parser.add_argument('-Y' , action="store_true" , help=
'''
Output as YAML.
Note that YAML may output a document start/end line "---" or "..."
'''
)
parser.add_argument('-P' , action="store_true" , help=
'''Output as pure output of py`print()` without newline end.'''
)
args = parser.parse_args()
iof = [None , None]
load = {
	
}

def loads(tree:str) :
	if args.y :
		tree = yamllib.safe_load(tree)
		return tree
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
def dump(todump) :
	if None : pass
	elif args.J : print(jsonlib.dumps(todump))
	elif args.Y : print(yamllib.dump(todump) , end='')
	elif args.T :
		try :
			print(tomllib.dumps(todump) , end='')
		except Exception :
			raise Exception("TOML" , textwrap.dedent(
				f'''
				Error when try to ouput TOML.
				If other formats is valid, maybe {toml_limits} in tree
				'''
			).replace('\n','').replace('\r',''))
	elif args.P : print(todump , end='')
	else : print(jsonlib.dumps(todump) , end='') #`-J` by default
