# draw.io Style Reference

These style strings are taken from his diagrams, with `points=[...]`
connection arrays and long embedded SVGs trimmed. Paste them into
`mxCell style` attributes.

## Containers

Plain boundary, or a panel such as "REST API" or "Backend Lambdas", with the
label at the top:

```text
rounded=0;whiteSpace=wrap;html=1;align=center;verticalAlign=top;
```

Light-gray panel for a subsystem or job group (use `#F5F5F5` for a subsystem
with a large title):

```text
rounded=0;whiteSpace=wrap;html=1;align=center;verticalAlign=top;fillColor=#F2F2F2;
```

AWS account group:

```text
shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_account;strokeColor=#CD2264;fillColor=none;verticalAlign=top;align=left;spacingLeft=30;fontColor=#CD2264;container=1;html=1;whiteSpace=wrap;
```

VPC group (AWS): use `grIcon=mxgraph.aws4.group_vpc` with
`strokeColor=#248814` (or the default blue on older diagrams).

Boundary title, the bold text label placed inside the top-right corner:

```text
text;html=1;align=center;verticalAlign=middle;autosize=1;strokeColor=none;fillColor=none;fontStyle=1;fontSize=14;
```

## Actors and externals

User group:

```text
shape=mxgraph.aws3.users;fillColor=#D2D3D3;verticalLabelPosition=top;verticalAlign=bottom;align=center;html=1;outlineConnect=0;
```

Identity provider (lock):

```text
shape=mxgraph.cisco19.lock;fillColor=#005073;strokeColor=none;verticalLabelPosition=bottom;verticalAlign=top;aspect=fixed;html=1;
```

External system or upstream IdP:

```text
ellipse;shape=cloud;whiteSpace=wrap;html=1;
```

## Services

AWS service (DynamoDB shown; swap `resIcon` and the fill for other services):

```text
shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.dynamodb;fillColor=#3334B9;gradientColor=#4D72F3;gradientDirection=north;strokeColor=#ffffff;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;aspect=fixed;
```

GCP services come from draw.io's GCP icon library, which inserts them as
`shape=image;image=data:image/svg+xml,...` cells. Insert them from the library
rather than hand-writing the SVG. Keep `verticalLabelPosition=bottom;
labelBackgroundColor=#ffffff`.

## Edges

Internal connection:

```text
edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=classic;
```

Read/write, with arrows on both ends:

```text
edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;startArrow=classic;endArrow=classic;
```

Internet traffic (dotted), labeled with the protocol through `value`:

```text
html=1;rounded=0;dashed=1;dashPattern=1 1;startArrow=classic;endArrow=none;fontSize=12;
```

## Fonts

`fontFamily=Helvetica`. 12 for labels, 14 for panel
titles, and 18-24 for diagram and subsystem titles.
