from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render


def get_page_filler():
    s = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse auctor fringilla arcu, id scelerisque turpis sodales eget. Nullam congue ligula et sapien vehicula, vitae sagittis elit euismod. Morbi convallis, neque non sagittis cursus, nunc risus accumsan elit, quis semper tellus elit in tortor. Suspendisse egestas auctor neque id euismod. Sed in rhoncus mi. Etiam sollicitudin urna eu elit consequat semper. Integer porttitor iaculis eros id dapibus. Fusce ut congue lorem'
    filler_list = s.split()
    return filler_list
