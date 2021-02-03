from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Sheet, Field, Style

# Usable functions


def get_objects_styles(objects):
    style_dict = {}
    for o in objects:
        style = o.style
        style_dict[o] = {
            'height': style.height,
            'width': style.width,
            'background-color': style.bgcolor,
            'color': style.txtcolor,
            'font-size': style.fontsize,
            'border': style.border
        }

    return style_dict


def generate_parent_structure(objects, parent=None):
    with_parent = {}
    structure = {}

    for o in objects:
        if o.parent is None or o.parent == parent:
            structure[o] = {}
        else:
            if o.parent not in with_parent:
                with_parent[o.parent] = []
            with_parent[o.parent].append(o)

    for k, v in with_parent.items():
        structure[k] |= generate_parent_structure(v, k)

    return structure


def get_div_layout(layout):
    div_layout = ""

    for k, v in layout.items():
        div_layout += """
    <div draggable="true" class="box %s" style="grid-area:%s">%s""" % (k.name, k.name, k.name)
        if len(v) > 0:
            div_layout += get_div_layout(v)
        div_layout += "</div>"

    return div_layout


def get_layout_from_fields(fields, parent=None):
    layout = []
    ret_layout = {}
    with_parent = {}
    layout_str = ""

    for f in fields:
        if f.parent is None or f.parent.name == parent:
            pointer = [f.positionX - 1, f.positionY - 1]
            for y in range(f.rowspan):
                while len(layout) - 1 < pointer[1]:
                    layout.append([])
                for x in range(f.colspan):
                    while len(layout[pointer[1]]) - 1 < pointer[0]:
                        layout[pointer[1]].append("")
                    layout[pointer[1]][pointer[0]] = f.name
                    pointer[0] += 1
                pointer[1] += 1
                pointer[0] = f.positionX - 1
        else:
            if f.parent not in with_parent:
                with_parent[f.parent] = []
            with_parent[f.parent].append(f)

    for r in layout:
        layout_str += '\"'
        for i in r:
            layout_str += "%s " % i
        layout_str += '\"\n'

    if parent is None:
        ret_layout['container'] = layout_str
    else:
        ret_layout[parent] = layout_str

    for k, f in with_parent.items():
        ret_layout |= get_layout_from_fields(f, k.name)

    return ret_layout


def generate_kanban(table_id):
    sheet = Sheet.objects.get(pk=table_id)
    fields = Field.objects.filter(sheet=table_id)

    fields.order_by('positionY', 'positionX')
    layout = get_layout_from_fields(fields)

    kanban = {
        'sheet': sheet,
        'fields': {
            'objects': get_objects_styles(fields),
            'layout': layout,
            'div_layout': get_div_layout(generate_parent_structure(fields))
        }
    }

    return kanban

# Views generators.


def index(request):
    all_tables = Sheet.objects.all()
    template = loader.get_template('index.html')
    context = {
        'tables': all_tables
    }
    return HttpResponse(template.render(context, request))


def view_table(request, table_id):
    """
    Generate a virtual list of fields.
    Then "print" it in html.
    Ex:
    L1-9 - Label field 1-9
    S1-9 - Sticker field 1-9

    {
    objects: [L1, L2, L3, S1, S2, S3],
    layout: [
        [L1, L2, L3],
        [S1, S1, S2],
        [S1, S1, S3]
    ]
    }

    """

    template = loader.get_template('kanban.html')
    context = generate_kanban(table_id)

    return HttpResponse(template.render(context, request))


def editor(request, editor_mode, editor_table=0):
    template = loader.get_template("editor.html")
    context = {}
    if editor_mode == "create":
        return HttpResponse("Create mode")
    elif editor_mode == "edit" and editor_table != 0:
        context = generate_kanban(editor_table)
        print(context['fields']['objects'])
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponse("No mode or no table selected")
