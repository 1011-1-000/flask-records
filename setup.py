import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="flask_records",
    version="0.0.8",
    author="leo",
    author_email="leo.anonymous@qq.com",
    description="Flask wrapper for the SQL Records",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PassWarer/flask-records",
    packages=['flask_records'],
    classifiers=[                                           # 关于包的其他元数据(metadata)
        "Programming Language :: Python :: 3",              # 该软件包仅与Python3兼容
        "License :: OSI Approved :: MIT License",           # 根据MIT许可证开源
        "Operating System :: OS Independent",               # 与操作系统无关
    ],
    install_requires=['Flask>=0.9',
                      'Flask-SQLAlchemy>=1.0',
                      'records>=0.5.3'],
    test_suite="tests"
)
