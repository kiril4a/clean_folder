from setuptools import setup, find_packages

setup(
    name='clean_folder',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'clean-folder=clean_folder.clean:main',
        ],
    },
    install_requires=[
        'transliterate',
        'patool',
    ],
    author='Kyrylo',
    description='Інструмент для очищення та організації папок',
)