"""First hug API (local, command-line, and HTTP access)"""
import hug


@hug.cli()
@hug.get(examples='name=Atilla&age=39')
@hug.local()
def your_name_is(name: hug.types.text, age: hug.types.number, hug_timer=3):
    """Print your name"""
    return {'message': f'Just to let you know that, your name is {name} and you are {age} years old!',
            'took': float(hug_timer)}


if __name__ == '__main__':
    your_name_is.interface.cli()