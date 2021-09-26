import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='extreme-tools',  
     version='0.1',
     author="ExtremeGrief",
     description="A Python module which adds basic tools like clear_console()",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/extremegrief1/extreme-tools",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )