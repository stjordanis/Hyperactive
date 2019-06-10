import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hyperactive",
    version="0.1.4",
    author="Simon Blanke",
    author_email="simon.blanke@yahoo.com",
    license="MIT",
    description="Meta heuristic optimization techniques for scikit-learn, XGBoost and Keras models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=["machine learning", "deep learning", "optimization", "data-science"],
    url="https://github.com/SimonBlanke/hyperactive",
    packages=["hyperactive"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
    ],
    install_requires=["numpy", "tqdm", "scikit-learn>=0.18"],
    test_suite="nose.collector",
    tests_require=["nose"],
)