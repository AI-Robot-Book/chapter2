from setuptools import setup

package_name = 'happy_action'

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
            'happy_action_server_node = happy_action.happy_action_server_node:main',
            'happy_action_client_node  = happy_action.happy_action_client_node:main'
        ],
    },
)
