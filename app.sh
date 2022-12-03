BOKEH_ALLOW_WS_ORIGIN=run-$DOMINO_RUN_ID.domino-compute.svc.cluster.local:80
python -m pip install -r requirements.txt --user
python -m panel serve app.py --address="localhost" --port=8888 --autoreload