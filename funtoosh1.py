import re
dv = """

+------------------------------------+-----------------------------------+
| likes                              | dislikes                          |
+------------------------------------+-----------------------------------+
| Meritocracy                        | Favoritism, ass-kissing, politics |
+------------------------------------+-----------------------------------+
| Healthy debates and collaboration  | Ego-driven rhetoric, drama and FUD|
|                                    | to get one's way                  |
+------------------------------------+-----------------------------------+
| Autonomy given by confident leaders| Micro-management by insecure      |
| capable of attracting top-tier     | managers compensating for a weak, |
| talent                             | immature team                     |
+------------------------------------+-----------------------------------+
| Fluid communication, brief, ad-hoc | Formal meetings, endless debate   |
| discussions, white-boarding, and   |                                   |
| quick but informed decisions       |                                   |
+------------------------------------+-----------------------------------+
| Where else can I help out?         | I'm blocked by..., I only know how|
|                                    | to...                             |
+------------------------------------+-----------------------------------+
| Getting things done.               | Contrived company culture         |
+------------------------------------+-----------------------------------+
| Clever and disruptive business     |                                   |
| ideas that solve real and immediate|                                   |
| needs in a marketplace             |                                   |
+------------------------------------+-----------------------------------+
| Software and system abstractions   | Hard-coding, brute-force          |
+------------------------------------+-----------------------------------+
| Frameworks and best-practices      | Hermetic code-base                |
+------------------------------------+-----------------------------------+
| Best tool for the job              | One size fits all                 |
+------------------------------------+-----------------------------------+
| Simple design                      | Over-engineering                  |
+------------------------------------+-----------------------------------+
| Leveraging open-source             | Re-inventing the wheel            |
+------------------------------------+-----------------------------------+
| Practical solutions to business    | Let's do this or use that because |
| core competency                    | it's new and cool                 |
+------------------------------------+-----------------------------------+
| Building solutions to current      | Over-emphasizing "nice-to-haves"  |
| business needs and customer demand | and conjecture                    |
+------------------------------------+-----------------------------------+

"""
gets = re.findall('[\w]*',dv)
for items in gets:
   print items
