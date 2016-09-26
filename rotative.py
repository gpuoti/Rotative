from  sphinx.application import Sphinx
import SCons.Builder

"""
Rotative add to sphinx a really minimal scons interface that let you build your html
documentation from restructured text content with 3 more line of code into your Sconstruct file.
Here is a simple example:

    import rotative

    env = rotative.register(Environment())
    doc_builder = env.rotative( source = 'source/conf.py')

"""

def __build_the_doc(target, source, env):
    doc_source = str(source[0])[:-8]
    conf_folder = doc_source
    out_folder = env['rotative']['out_folder']
    doc_tree_folder = out_folder + '/' + env['rotative']['doctree_folder']
    doc_builder = 'html'
    builder = Sphinx( doc_source, conf_folder, out_folder, doc_tree_folder, doc_builder)
    builder.build()
    return None

builder = SCons.Builder.Builder( action = __build_the_doc, src_suffix = '')                    


def register (scons_environment):
    scons_environment['BUILDERS']['rotative'] = builder
    scons_environment['rotative'] = {}
    scons_environment['rotative']['out_folder'] = 'user-doc'
    scons_environment['rotative']['doctree_folder'] = 'doctree'
    return scons_environment