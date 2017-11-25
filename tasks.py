from invoke import task

@task
def build(ctx):
    '''Build Docker images defined in `docker-compose.yml`.'''
    ctx.run('docker-compose build')


@task(pre=[build])
def up(ctx):
    '''Run the containers as defined in `docker-compose.yml`.
    '''
    ctx.run('docker-compose up -d', pty=True)


@task
def down(ctx):
    '''Stop all containers.'''
    ctx.run('docker-compose down')
