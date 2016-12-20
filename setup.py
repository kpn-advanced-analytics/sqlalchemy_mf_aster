from setuptools import setup


setup(
    name='sqlalchemy_mf_aster',
    version=0.1,
    description="Aster Modelfactory for SQLAlchemy",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Database :: Front-Ends',
    ],
    keywords='SQLAlchemy Aster Modelfactory',
    author='Maria Vechtomova',
    author_email='',
    license='MIT',
    packages=['sqlalchemy_mf_aster'],
    include_package_data=True,
    tests_require=['nose >= 0.11'],
    test_suite='nose.collector',
    zip_safe=False,
    entry_points={
        'sqlalchemy.dialects': [
            'aster = sqlalchemy_aster.jdbc:AsterDialect_jdbc',
            'aster.jdbc = sqlalchemy_aster.jdbc:AsterDialect_jdbc',
        ]
    }
)
