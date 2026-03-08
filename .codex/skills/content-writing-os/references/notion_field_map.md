# Notion Field Map

## Research Bank

Data source:
- `collection://2f45eb94-8864-801b-a248-000b106b02c4`

Required input fields:
1. `Title`
2. `Link`
3. `Why it matters`

Preferred fields:
1. `Evidence Links`
2. `Content Angle`
3. `Hook`
4. `Research Type`
5. `Editorial Decision`
6. `Score`

## Content Library

Data source:
- `collection://2f45eb94-8864-8040-aa3a-000b4dc54386`

Generated record defaults:
1. `Status=Not started`
2. `QA Ready=__NO__`
3. `Primary Research=[<research_page_url>]`

Piece-specific mapping:

1. Medium
- `Asset Role=Core`
- `Content Type=Blog/Medium`

2. Newsletter
- `Asset Role=Core`
- `Content Type=Newsletter Issue`

3. LinkedIn A
- `Asset Role=Derivative`
- `Content Type=Linkedin Post`
- `Parent Asset=[<newsletter_page_url>]`

4. LinkedIn B
- `Asset Role=Derivative`
- `Content Type=Linkedin Post`
- `Parent Asset=[<newsletter_page_url>]`
