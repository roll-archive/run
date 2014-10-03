from packgram.project import ProjectModule


class ProjectModule(ProjectModule):

    # Attributes

    author = 'roll'
    author_email = 'roll@respect31.com'
    copyright = 'Copyright (c) 2014 Respect31 <post@respect31.com>'
    data_files = [('/etc/bash_completion.d', ['data/run.sh'])]
    description = 'Run is a program to run tasks from files.'
    development_requires = ['packgram>=0.23']
    entry_points = {'console_scripts': ['run = run:program']}
    github_user = 'respect31'
    install_requires = [
        'box>=0.42', 'color>=0.3',
        'dialog>=0.4', 'find>=0.3', 'render>=0.2', 'sheldon>=0.3', ]
    interpreters = ['3.3', '3.4']
    license = 'MIT License'
    name = 'run'
    platforms = ['Unix']
    pypi_name = 'runfile'
    pypi_password_secure = 'JaTeiyjnimmtwhbdfPMZZdtp+5S920vb0HobJWL1QQjHVAo5Hwt0kTWYG+zjDrpWUL+NanVNqhQA8xnvWKbI5cZ+n3PvS7KFbgn6XcTYfeEGyEdYUFi0sXaUsgcfke+9nyMBDLoRH2M7TGqpLY2dmXk5C0h0RMkkAPjxgZCan94='
    tests_require = ['nose', 'coverage']
    test_suite = 'nose.collector'
    version = '0.36.0'
