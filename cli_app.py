import argparse

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Group, Professor, Student, Subject

from db import URI

engine = create_engine(URI)
Session = sessionmaker(bind=engine)
session = Session()

# actions and models
actions = ["create", "list", "update", "remove"]
models_ = ["Group", "Professor", "Student", "Subject"]

# argument parser
parser = argparse.ArgumentParser(description="CLI app for CRUD operations with DB tables: ")
parser.add_argument("-a", "--action", choices=actions, required=True, help="The action to perform")
parser.add_argument("-m", "--model", choices=models_, required=True, help="The model to use for the action")
parser.add_argument("-n", "--name", type=str, help="The name of the model instance")
parser.add_argument("-i", "--id", type=int, help="The id of the model instance")
parser.add_argument("-g", "--group_id", type=int, help="The id of the group - used for the Student model instance")
parser.add_argument("-p", "--professor_id", type=int,
                    help="The id of the Professor - used for the Subject model instance")

# Parse the arguments
args = parser.parse_args()
# print(args)
# parsed_args = vars(args)
"""
Usage example:
python3 cli_app.py --action create --model Student --name 'New Student' --group_id 1 - create new student with name 'New Student' and group_id 1
python3 cli_app.py -a create -m Subject -n 'New One' -p 1  - create new subject with name 'New One' and professor_id 1

python3 cli_app.py --action list -m Student - list all students
python3 cli_app.py -a list -m Subject - list all subjects

python3 cli_app.py --action update -m Student --id 52 --name 'Updated' - update student with id 52 to name 'Updated'
python3 cli_app.py -a update -m Professor -i 1 -n 'Professor Updated' - update professor with id 1 to name 'Professor Updated'

python3 cli_app.py --action remove -m Student -i 51 - remove student with id 51
python3 cli_app.py -a remove -m Group --id 6 - remove group with id 6

"""


def validate_args_create_update(args):
    if not args.name:
        print("Please provide a name for the model instance")
        return False

    if args.model == 'Student' and not args.group_id:
        print("Please provide a group_id for the Student model instance")
        return False

    if args.model == 'Subject' and not args.professor_id:
        print("Please provide a professor_id for the Subject model instance")
        return False
    return True


def success_create_message(args):
    if args.model == 'Student':
        return f"Created {args.model} with name {args.name} and group_id {args.group_id}"
    if args.model == 'Subject':
        return f"Created {args.model} with name {args.name} and professor_id {args.professor_id}"
    return f"Created {args.model} with name {args.name}"


model_class = globals()[args.model]
# model_class = getattr(models, args.model)

# actions
if args.action == "create":
    if validate_args_create_update(args):
        if args.model == 'Student':
            model_instance = model_class(name=args.name, group_id=args.group_id)
        elif args.model == 'Subject':
            model_instance = model_class(name=args.name, professor_id=args.professor_id)
        else:
            model_instance = model_class(name=args.name)
        session.add(model_instance)
        session.commit()
        print(success_create_message(args))

elif args.action == "list":
    model_instances = session.query(model_class).all()
    print(f"Listing all {args.model}s:")
    for model_instance in model_instances:
        if args.model == 'Student':
            print(f"{model_instance.id}: {model_instance.name}, Group: {model_instance.group_id}")
        elif args.model == 'Subject':
            print(f"{model_instance.id}: {model_instance.name}, Professor: {model_instance.professor_id}")
        else:
            print(f"{model_instance.id}: {model_instance.name}")

elif args.action == "update":
    if args.id and args.name:
        # model_instance = session.query(model_class).get(args.id)
        model_instance = session.get(model_class, args.id)
        if model_instance:
            model_instance.name = args.name
            session.add(model_instance)
            session.commit()
            print(f"Updated {args.model} with id {args.id} to name {args.name}")
        else:
            print(f"No {args.model} found with id {args.id}")
    else:
        print("Please provide an id and a name for the model instance")

elif args.action == "remove":
    if args.id:
        # model_instance = session.query(model_class).get(args.id)
        model_instance = session.get(model_class, args.id)
        if model_instance:
            session.delete(model_instance)
            session.commit()
            print(f"Removed {args.model} with id {args.id}")
        else:
            print(f"No {args.model} found with id {args.id}")
    else:
        print("Please provide an id for the model instance")
