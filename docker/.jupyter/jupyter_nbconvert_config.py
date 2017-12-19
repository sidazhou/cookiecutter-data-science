# # not working, tried one line at a time
# NameError: name 'Exporter' is not defined
# Exporter.preprocessors += ['jupyter_contrib_nbextensions.nbconvert_support.CodeFoldingPreprocessor']
# Exporter.preprocessors += ['jupyter_contrib_nbextensions.nbconvert_support.pre_codefolding']
# c.Exporter.preprocessors.append('jupyter_contrib_nbextensions.nbconvert_support.pre_codefolding')
c.Exporter.preprocessors.append('jupyter_contrib_nbextensions.nbconvert_support.CodeFoldingPreprocessor')

# working for cmd line
c.CodeFoldingPreprocessor.remove_folded_code=True
