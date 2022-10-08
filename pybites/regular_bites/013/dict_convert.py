from collections import namedtuple
from datetime import datetime
import json


blog = dict(
    name="PyBites",
    founders=("Julian", "Bob"),
    started=datetime(year=2016, month=12, day=19),
    tags=["Python", "Code Challenges", "Learn by Doing"],
    location="Spain/Australia",
    site="https://pybit.es",
)

# define namedtuple here
blog_nt = namedtuple("blog_nt", blog.keys())


def dict2nt(dict_):
   return blog_nt._make(dict_.values())


def nt2json(nt):
    return json.dumps(nt._asdict(), default=str)
