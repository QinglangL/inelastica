def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration
    from numpy.distutils.system_info import get_info

    config = Configuration('Inelastica', parent_package, top_path)

    config.add_subpackage('fortran')
    config.add_subpackage('io')
    config.add_subpackage('physics')
    config.make_config_py()
    return config

if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(**configuration(top_path='').todict())
