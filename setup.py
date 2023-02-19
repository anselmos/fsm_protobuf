from setuptools import setup

setup(
    name='fsm_proto',
    version='0.1.0',
    description='A protobuf package for FSM services',
    url='https://github.com/anselmos/fsm_protobuf',
    author='Anselmos',
    author_email='anselmos@github.com',
    license='MIT',
    packages=['fsm_proto'],
    install_requires=[
        "grpcio",
        "grpcio-tools"
    ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.11',
    ],
)
