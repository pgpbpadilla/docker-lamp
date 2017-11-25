from invoke import task

@task
def up(ctx):
    '''Run the containers as defined in `docker-compose.yml`.
    '''
    ctx.run('docker-compose up -d', pty=True)
