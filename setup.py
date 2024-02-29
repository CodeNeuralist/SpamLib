from setuptools import setup, find_packages

setup(
    name='spam_classifier_library',  # Имя вашего пакета
    version='0.1.0',  # Версия вашего пакета
    packages=find_packages(),  # Список пакетов для включения в ваш пакет
    author='Кирилл',  # Ваше имя
    author_email='totoshkus@gmail.com',  # Ваш адрес электронной почты
    description='A library for spam classification',  # Краткое описание вашего пакета
    long_description=open('README.md').read(),  # Длинное описание вашего пакета (из файла README.md)
    long_description_content_type='text/markdown',  # Тип содержимого вашего длинного описания
    url='https://github.com/yourusername/yourproject',  # URL-адрес вашего репозитория на GitHub
    install_requires=[
        'torch>=1.9.0',
        'scikit-learn>=0.24.2',
    ],  # Список зависимостей вашего пакета
    classifiers=[  # Классификаторы, которые описывают ваш пакет
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
