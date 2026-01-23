from setuptools import setup, find_packages

setup(
    name="quantum-measurement-tomography",
    version="0.1.0",
    description="Measurement theory, SIC POVMs, and single-qubit quantum state tomography",
    author="Kishore",
    python_requires=">=3.9",
    install_requires=[
        "numpy>=1.23",
        "scipy>=1.9",
        "plotly>=5.18",
        "jupyter>=1.0",
        "notebook>=7.0",
        "ipykernel>=6.25",
    ],
    packages=find_packages(),
    include_package_data=True,
)
