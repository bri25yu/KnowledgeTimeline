from calendar import month_abbr

from django.shortcuts import render

from graph.models import Group, Node



def index(request):
    groups_query = request.GET.get("groups", "")
    if groups_query:
        group_ids = map(lambda s: int(s[5:]), groups_query.split(","))
    else:
        group_ids = list(Group.objects.values_list("id", flat=True))

    nodes = Node.objects \
        .filter(group__id__in=group_ids) \
        .order_by("year", "month")

    groups = [
        {"id": f"group{g.id}", "color": g.color, "name": g.name}
        for g in Group.objects.all()
    ]

    context = {
        "nodes": nodes,
        "groups": groups,
    }
    return render(request, "graph/index.html", context)
