divert(-1)
define(`__code__', _mc_ `$1' _mc_)
define(`__md_code__', changequote([,])[changequote([,])```changequote(`,')]changequote(`,'))
define(`_mc_', `__md_code__')
changecom(`>>', `<<')
define(`__link__', [`$1']($1))
define(`__flink__', [`__code__($1)']($1))
define(`__more_details__',
` More details

> Enter sub directories to get more details for the specific module.'
)
define(`__codeitemlist__', `ifelse(`$#', `0', , `$#', `1', `__code__(`$1')', `__code__(`$1') __codeitemlist__(shift($@))')')
define(`__md_table_title__', `ifelse(`$#', `0', , `$#', `1', ``$1'', ``$1' | __md_table_title__(shift($@))')')
define(`__md_table_spline__', `ifelse(`$#', `0', , `$#', `1', `-', `- | __md_table_spline__(shift($@))')')
define(`__doing__', `⟳')
define(`__path_title__', ifelse(__path__, `', `', [<code>__path__</code>]()))
define(`__title__', __git__ __path_title__)
define(`__self__', `[__git__](__relative_root__)')
divert(-0)dnl
# __title__
[yaml , toml] to json

## About

Nowadays there 3 mainstream human-readable, structurized, and **non-tag-basic** format :

- _mc_ JSON _mc_
- _mc_ YAML _mc_
- _mc_ TOML _mc_

_mc_ JSON _mc_ is the most machine friendly and the most grammar-strict,
and the earliest one.
It lead to some subtle differences in development ecosystem.
*E.g.* for python3 :

-  _mc_ json _mc_  is in standard library set and completly support *json* format file
- *yaml* was supported by 3-party libraries, the "most offical" one is PyYAML
-  _mc_ tomllib _mc_  became a part of python standard library since *3.12*,
	but no dump function in it.

After all, it is recommanded always send data to process in  _mc_ JSON _mc_  format.
And if they were stored in  _mc_ YAML _mc_   _mc_ TOML _mc_  for human friendly usage,
convert them.

## Some details

The main function of __self__ is converting:

> [yaml , toml] to json

But infact __self__ can transform each one to each other or itself.

Without any option to specifiy the input format,
__self__ will try _mc_ JSON _mc_ 1stly, _mc_ TOML _mc_ 2ndly,
and _mc_ YAML _mc_ at last.
Because it is easily to make _mc_ YAML _mc_ to treat the whole document
or a large block as a string, even if they are in other formats.
