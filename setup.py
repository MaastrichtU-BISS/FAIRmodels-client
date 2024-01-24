from setuptools import setup, find_packages

setup(
  name='fair4ai_client',
  version='0.1.0',
  description='FAIR4AI Client Package',
  packages=find_packages(),
  install_requires=[
    'skl2onnx==1.16.0',
    'requests==2.31.0',
    'keyring==24.3.0'
  ]
)