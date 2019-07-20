import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
        name='convolution_overlap_add',
        version='0.1',
        script=['convolution_overlap_add'],
        author='Vinicius Mesquita',
        author_email='viniciusmesquita@poli.ufrj.br',
        description='Convolution using overlap-add method',
        long_description=long_description,
        long_description_content_type='text/markdown',
        url='https://github.com/mesquita/convolution_overlap_add',
        packages=setuptools.find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
)
        
