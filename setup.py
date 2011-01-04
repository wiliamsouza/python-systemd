from distutils.core import setup
import os

from systemd import get_version


# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)

for dirpath, dirnames, filenames in os.walk('systemd'):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if '__init__.py' in filenames:
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)
    elif filenames:
        prefix = dirpath[13:] # Strip "systemd/" or "systemd\"
        for f in filenames:
            data_files.append(os.path.join(prefix, f))


setup(name='python-systemd',
      version=get_version().replace(' ', '-'),
      description='Systemd interfaces wrapper',
      author='Wiliam Souza',
      author_email='wiliam@mandriva.com',
      url='',
      download_url='',
      package_dir={'systemd': 'systemd'},
      packages=packages,
      package_data={'systemd': data_files},
      classifiers=['Development Status :: 1 - Planning',
                   'Intended Audience :: Developers',
                   'License :: ',
		   'Operating System :: POSIX :: Linux',
                   'Programming Language :: Python',
                   'Topic :: Libraries :: Python Modules',]
      )

