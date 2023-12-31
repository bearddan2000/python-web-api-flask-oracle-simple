from flask import Flask, request
import logging
from client import Endpoint

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route('/')
def smoke_test():
    d = {'hello': 'world'}
    return {'results': d}

@app.route('/help', methods=['GET'])
def routes_info():
    """Show all registered routes with endpoints and methods."""
    routes = []

    rules = list(app.url_map.iter_rules())
    if not rules:
        logging.warning("No routes were registered.")
        return  {"results": routes}

    ignored_methods = set()

    rules = sorted(rules, key=lambda rule: sorted(rule.methods))  # type: ignore

    rule_methods = [
        ", ".join(sorted(rule.methods - ignored_methods))  # type: ignore
        for rule in rules
    ]

    headers = ("Endpoint", "Methods", "Rule")
    widths = (
        max(len(rule.endpoint) for rule in rules),
        max(len(methods) for methods in rule_methods),
        max(len(rule.rule) for rule in rules),
    )
    widths = [max(len(h), w) for h, w in zip(headers, widths)]
    row = "{{0:<{0}}}  {{1:<{1}}}  {{2:<{2}}}".format(*widths)

    routes.append(row.format(*headers).strip())
    routes.append(row.format(*("-" * width for width in widths)))

    for rule, methods in zip(rules, rule_methods):
        routes.append(row.format(rule.endpoint, methods, rule.rule).rstrip())
    return  {"results": routes}

@app.route('/dog')
def get_all():
    results = endpoint.get_all()
    return {'results': results}

@app.route('/dog/breed/<breed>', methods=['GET', 'DELETE', 'POST'])
def filter_del_upd_by_breed(breed: str):
    results = []
    if request.method == 'GET':
        results = endpoint.filter_by('breed', breed)
    elif request.method == 'DELETE':
        results = endpoint.delete('breed', breed)
    elif request.method == 'POST':
        results = endpoint.update('breed', breed)
    return {'results': results}

@app.route('/dog/color/<color>', methods=['GET', 'DELETE', 'POST'])
def filter_del_upd_by_color(color: str):
    results = []
    if request.method == 'GET':
        results = endpoint.filter_by('color', color)
    elif request.method == 'DELETE':
        results = endpoint.delete('color', color)
    elif request.method == 'POST':
        results = endpoint.update('color', color)
    return {'results': results}

@app.route('/dog/id/<int:id>', methods=['GET', 'DELETE', 'POST'])
def filter_del_upd_by_id(id: int):
    results = []
    if request.method == 'GET':
        results = endpoint.filter_by('id', id)
    elif request.method == 'DELETE':
        results = endpoint.delete('id', id)
    elif request.method == 'POST':
        results = endpoint.update('id', id)
    return {'results': results}

@app.route('/dog/breed/<breed>/color/<color>', methods=['PUT'])
def ins_by_breed(breed: str, color: str):
    results = endpoint.insert(breed, color)
    return {'results': results}

if __name__ == "__main__":
    endpoint = Endpoint()
    app.run(host ='0.0.0.0', port = 5000, debug = True)
