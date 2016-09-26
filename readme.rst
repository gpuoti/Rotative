========
Rotative
========

Rotative is a extremelly simple interface that let scons build html documentation from RestructuredText. The code required into your Sconstruct file is really minimal:

.. code-block:: python 

    import rotative

    env = rotative.register(Environment())
    doc_builder = env.rotative( source = 'source/conf.py')

of cource you need to import rotative flavors then register rotative into a newly created environment or into the one you already know to let the builde be available. Once rotative is available into your environment, declare your build action specifying the sphinx configuration file to use. 
Rotative implicitelly assumes the documentation source is based into the same folder containing the configuration file.

More options
------------

More options are available through environment properties. Rotative properties are available as entry into the dictionary stored as **'rotative'** into the environment dictionary. 
Available properties are:

    out_folder
        relative path to the folder that will contain the built documentation

    doctree_folder
        relative path based on **out_folder** to the folder that will contain the doctree