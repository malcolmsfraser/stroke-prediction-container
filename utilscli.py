#!/usr/bin/env python
import click
import mlib
import requests
from predict import create_payload

@click.group()
@click.version_option("1.0")
def cli():
    """Machine Learning Utility Belt"""


@cli.command("retrain")
@click.option("--tsize", default=0.1, help="Test Size")
def retrain(tsize):
    """Retrain Model
    You may want to extend this with more options, such as setting model_name
    """

    click.echo(click.style("Retraining Model", bg="green", fg="white"))
    accuracy, model_name = mlib.retrain(tsize=tsize)
    click.echo(
        click.style(f"Retrained Model Accuracy: {accuracy}", bg="blue", fg="white")
    )
    click.echo(click.style(f"Retrained Model Name: {model_name}", bg="red", fg="white"))


@cli.command("predict")
@click.option("--host", default="http://localhost:8080/predict", help="Host to query")
def mkrequest(host):
    """Sends prediction to ML Endpoint"""
    
    payload = create_payload()
    click.echo(click.style(f"Querying host {host} with payload: \n{payload}",
        bg="green", fg="white"))
    result = requests.post(url=host, json=payload)
    click.echo(click.style(f"result: {result.text}", bg="red", fg="white"))


if __name__ == "__main__":
    cli()