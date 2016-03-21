import click


def handle_click_http_exception(e):
    click.secho("{0}".format(e), fg='red', bold=True)
    exit(1)
