from setuptools import find_packages, setup

package_name = 'fsr_pub'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='taylor3527',
    maintainer_email='taylor3527@yonsei.ac.kr',
    description='FSR Publishing',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	'talker = fsr_publisher.py:main',
        ],
    },
)
