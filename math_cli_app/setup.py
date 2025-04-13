from setuptools import setup, find_packages

setup(
    name="math_cli_app",
    version="0.1.0",
    packages=find_packages(include=['math_cli_app', 'math_cli_app.*']),
    python_requires=">=3.8",
    install_requires=[],
    extras_require={
        'test': [
            'pytest>=7.4.3',
            'pytest-cov>=4.1.0',
            'codecov>=2.1.13',
        ],
    },
) 