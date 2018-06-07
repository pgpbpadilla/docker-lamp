from invoke import task
import os, shutil

@task
def build(ctx):
    '''Build Docker images defined in `docker-compose.yml`.'''
    ctx.run('docker-compose build')

@task
def clean(ctx):
    '''Remove data created by previous run'''
    print('Clean up old data ...')
    tmp_data_dir = './db/data'
    if os.path.exists(tmp_data_dir):
        shutil.rmtree(tmp_data_dir)
    print('It worked!')

@task(pre=[clean, build])
def up(ctx):
    '''Run the containers as defined in `docker-compose.yml`.
    '''
    ctx.run('docker-compose up -d', pty=True)


@task
def down(ctx):
    '''Stop all containers.'''
    ctx.run('docker-compose down')
