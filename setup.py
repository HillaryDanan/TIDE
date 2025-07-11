from setuptools import setup, find_packages

setup(
    name="tide-framework",
    version="0.1.0",
    author="Hillary Danan",
    author_email="your.email@example.com",
    description="Temporal-Internal Dimensional Encoding: Cognitive architecture patterns for AI systems",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/HillaryDanan/TIDE",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.19.0",
        "scipy>=1.5.0",
        "matplotlib>=3.3.0",
        "torch>=1.9.0",
        "pandas>=1.1.0",
        "seaborn>=0.11.0",
    ],
)
