from setuptools import setup

package_name = 'happy'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mini',
    maintainer_email='mini@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'happy_node = happy.happy_node:main',
            'happy_node2 = happy.happy_node2:main',
            'happy_node3 = happy.happy_node3:main',
            'happy_node4 = happy.happy_node4:main',
            'happy_node5 = happy.happy_node5:main',
        ],
    },
)
