import os

c = get_config()  # pyright: reportUndefinedVariable=false
c.NotebookApp.ip = "0.0.0.0"
c.NotebookApp.port = 8888
c.NotebookApp.open_browser = False

# https://github.com/jupyter/notebook/issues/3130
c.FileContentsManager.delete_to_trash = False

# this is commented out, because the reverse proxy handles this. See secHeaders middleware in traefik/data/dynamic_conf.yml
# c.NotebookApp.tornado_settings = {
#     'cookie_options': {"SameSite": "None", "Secure": True},
#     'headers': {
#         'Content-Security-Policy': "frame-ancestors 'self' http://localhost:80 http://127.0.0.1:80 http://localhost:8000 http://127.0.0.1:8000"
#     }
# }
# c.NotebookApp.disable_check_xsrf = True

c.NotebookApp.terminals_enabled = False
