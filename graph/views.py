from calendar import month_abbr
from collections import Counter

from django.shortcuts import render

from graph.models import Group, Node


X_EM_PER_PAPER = 17
Y_EM_PER_YEAR = 8
HORIZONTAL_ORDERING = [-1, 1, -2, 2, -3, 3]


def index(request):
    groups_query = request.GET.get("groups", "")
    if groups_query:
        group_ids = map(lambda s: int(s[5:]), groups_query.split(","))
    else:
        group_ids = list(Group.objects.values_list("id", flat=True))

    node_db_objects = Node.objects.filter(group__id__in=group_ids)

    years = set(node_db_objects.values_list("year", flat=True))
    year_start, year_end = int(min(years)) - 1, int(max(years)) + 1
    year_to_ypos = {
        y: (y - year_start) * Y_EM_PER_YEAR
        for y in range(year_start, year_end+1)
    }
    years = [
        {"value": y, "y_pos": v}
        for y, v in year_to_ypos.items()
    ]

    timeline_height = year_to_ypos[year_end] - year_to_ypos[year_start] + Y_EM_PER_YEAR

    seen_years = Counter()
    nodes = []
    for node in node_db_objects:
        x_pos = HORIZONTAL_ORDERING[seen_years[node.year]]
        seen_years[node.year] += 1
        nodes.append((
            {
                "x_pos": x_pos * X_EM_PER_PAPER,
                "y_pos": year_to_ypos[int(node.year)],
                "id": f"node{node.id}",
                "month": month_abbr[int(node.month)],
            },
            node,
        ))

    groups = [
        {"id": f"group{g.id}", "color": g.color, "name": g.name}
        for g in Group.objects.all()
    ]

    context = {
        "nodes": nodes,
        "timeline_height": timeline_height,
        "years": years,
        "groups": groups,
    }
    return render(request, "graph/index.html", context)
