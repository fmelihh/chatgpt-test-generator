from setuptools import setup, find_packages


setup(
    name='chatgpt_test_generator',
    version='0.1',
    license='MIT',
    author="Furkan Melih Ercan",
    author_email='furkanmelihercan.98@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/fmelihh/chatgpt-test-generator',
    keywords='ai based test generation tool',
    install_requires=[
          'toml',
          'openai',
      ],
)
