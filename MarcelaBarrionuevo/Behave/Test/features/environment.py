import yaml

global generic_data

# Generic data
generic_data = yaml.load(open('configuration/config.yml'))


def before_all(context):
    # print("*********Before All********")
    context.host = generic_data['host']
    context.method = generic_data['method']
    context.code = generic_data['code']
    print(context.host)
    print(context.method)
    print(context.code )


def after_feature(context, feature):
    if 'test2' in feature.tags:
        print("///////feature TEST 1 ALL///////")
    if 'Test' in feature.name:
        print("///////feature TEST ALL///////")

def before_feature(context, feature):
    if 'test1' in feature.tags:
        print("///////feature TEST 1 ALL///////")
    if 'Test' in feature.name:
        print("///////feature TEST ALL///////")

def before_scenario(context, scenario):
    if 'tagtest' in scenario.tags:
        print("///////Scenario tag///////")
    if 'marce' in scenario.name:
        print("///////feature TEST TEST///////")

def before_step(context, step):
    print("STEP", step.name)
    print("KEYWORD", step.keyword)
    print("STATUS", step.status)

